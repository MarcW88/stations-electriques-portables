#!/usr/bin/env python3
"""Build JSON-LD from public HTML only; safe to rerun before deployment."""
import argparse
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = 'https://stations-electriques-portables.fr/'
NAME = 'Stations Électriques Portables'
BLOCK = re.compile(r'<script\s+type="application/ld\+json"\s+id="site-structured-data">.*?</script>\s*', re.S)
VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}

class Node:
    def __init__(self, tag='', attrs=()):
        self.tag, self.attrs, self.children = tag, dict(attrs), []
    def find(self, tag=None, cls=None):
        found = []
        for child in self.children:
            if isinstance(child, Node):
                if (tag is None or child.tag == tag) and (cls is None or cls in child.attrs.get('class','').split()):
                    found.append(child)
                found.extend(child.find(tag, cls))
        return found
    def text(self):
        return re.sub(r'\s+', ' ', ''.join(c.text() if isinstance(c, Node) else c for c in self.children)).strip()

class Document(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.root = Node(); self.stack = [self.root]; self.feed(source)
    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs); self.stack[-1].children.append(node)
        if tag not in VOID: self.stack.append(node)
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID: self.handle_endtag(tag)
    def handle_endtag(self, tag):
        for i in range(len(self.stack)-1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]; break
    def handle_data(self, data): self.stack[-1].children.append(data)

def graph(source):
    root = Document(source).root
    canonical = [n.attrs['href'] for n in root.find('link') if n.attrs.get('rel') == 'canonical']
    assert len(canonical) == 1, 'Exactly one canonical required'
    url = canonical[0]; assert url.startswith(SITE), url
    main = root.find('main')[0]
    heading = main.find('h1')[0].text()
    description = next((n.attrs.get('content','') for n in root.find('meta') if n.attrs.get('name') == 'description'), '')
    path = urlsplit(url).path
    parts = [p for p in path.split('/') if p]
    family = parts[0] if parts else ''
    collection = len(parts) == 1 and family in {'guides','comparatifs','usages','marques','modeles','accessoires','solaire','puissance-capacite'}
    editorial = len(parts) > 1 and family in {'guides','comparatifs','usages','marques','accessoires','solaire','puissance-capacite'}
    kind = 'CollectionPage' if collection else 'AboutPage' if family == 'a-propos' else 'ContactPage' if family == 'contact' else 'ItemPage' if family == 'modeles' and len(parts)>1 else 'WebPage'
    page = {'@type':kind, '@id':url+'#webpage', 'url':url, 'name':heading, 'description':description, 'inLanguage':'fr-FR', 'isPartOf':{'@id':SITE+'#website'}}
    nodes = [{'@type':'WebSite','@id':SITE+'#website','url':SITE,'name':NAME,'inLanguage':'fr-FR'},page]
    # Mark only the breadcrumb actually displayed in the page.
    crumbs = main.find('nav','breadcrumb')
    if crumbs:
        items = []
        for a in crumbs[0].find('a'):
            items.append({'@type':'ListItem','position':len(items)+1,'name':a.text(),'item':urljoin(url,a.attrs['href'])})
        current = [n for n in crumbs[0].find('span') if 'sep' not in n.attrs.get('class','').split()]
        items.append({'@type':'ListItem','position':len(items)+1,'name':current[-1].text() if current else heading,'item':url})
        nodes.append({'@type':'BreadcrumbList','@id':url+'#breadcrumb','itemListElement':items})
        page['breadcrumb'] = {'@id':url+'#breadcrumb'}
    article_nodes = main.find('article','content-main')
    body = article_nodes[0] if article_nodes else main
    images = [urljoin(url,n.attrs['src']) for n in body.find('img') if n.attrs.get('src') and n.attrs.get('alt','').strip()]
    if images: page['primaryImageOfPage'] = {'@type':'ImageObject','url':images[0]}
    if editorial:
        article = {'@type':'Article','@id':url+'#article','headline':heading,'description':description,'inLanguage':'fr-FR','mainEntityOfPage':{'@id':page['@id']}}
        if images: article['image'] = list(dict.fromkeys(images))
        if family == 'marques':
            brand_name = main.find('nav','breadcrumb')[0].find('span')[-1].text()
            article['about'] = {'@type':'Brand','name':brand_name}
        nodes.append(article); page['mainEntity'] = {'@id':article['@id']}
    if kind == 'ItemPage':
        product = {'@type':'Product','@id':url+'#product','name':heading,'description':description,'url':url,'mainEntityOfPage':{'@id':page['@id']}}
        # Only the real product photograph, never a generic generated illustration.
        photos = main.find('figure','product-photo')
        if photos and photos[0].find('img'): product['image'] = urljoin(url,photos[0].find('img')[0].attrs['src'])
        specs = []
        for table in main.find('table','spec-table'):
            for row in table.find('tr'):
                cells = row.find('td')
                if len(cells) != 2: continue
                label,value = (c.text() for c in cells)
                if label == 'Marque': product['brand'] = {'@type':'Brand','name':value}
                elif value: specs.append({'@type':'PropertyValue','name':label,'value':value})
        if specs: product['additionalProperty'] = specs
        nodes.append(product); page['mainEntity'] = {'@id':product['@id']}
    if family == 'calculateur-autonomie':
        app = {'@type':'WebApplication','@id':url+'#application','name':heading,'url':url,'description':description,'inLanguage':'fr-FR','applicationCategory':'UtilitiesApplication','operatingSystem':'Web browser'}
        nodes.append(app);page['mainEntity'] = {'@id':app['@id']}
    # Document order, not a product ranking. Only visible links to existing site pages.
    if collection or family == 'comparatifs' and editorial:
        links = []; seen = set()
        for a in body.find('a'):
            href = a.attrs.get('href',''); target = urljoin(url,href)
            if not href.startswith('/') or '#' in target or target == url or target in seen: continue
            target_parts = [p for p in urlsplit(target).path.split('/') if p]
            if collection and (not target_parts or target_parts[0] != family): continue
            if not collection and not target.startswith(SITE+'modeles/'): continue
            label = a.find('h3') or a.find('h2')
            name = label[0].text() if label else a.text()
            if not name: continue
            seen.add(target); links.append({'@type':'ListItem','position':len(links)+1,'name':name,'url':target})
        if links:
            listing = {'@type':'ItemList','@id':url+'#list','itemListOrder':'https://schema.org/ItemListUnordered','numberOfItems':len(links),'itemListElement':links}
            nodes.append(listing)
            if collection:page['mainEntity'] = {'@id':listing['@id']}
            else:article['mainEntity'] = {'@id':listing['@id']}
    return {'@context':'https://schema.org','@graph':nodes}

def validate(data):
    assert data['@context'] == 'https://schema.org'
    nodes = data['@graph']; ids = {n['@id'] for n in nodes}; assert len(ids) == len(nodes)
    def visit(value):
        if isinstance(value,dict):
            if set(value) == {'@id'}: assert value['@id'] in ids, value
            assert not {'offers','aggregateRating','review','datePublished','dateModified','author'} & value.keys()
            for v in value.values():visit(v)
        elif isinstance(value,list):
            for v in value:visit(v)
    visit(data)
    for node in nodes:
        if 'itemListElement' in node:
            assert [e['position'] for e in node['itemListElement']] == list(range(1,len(node['itemListElement'])+1))
    return data

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
    pages = sorted([ROOT/'index.html',*ROOT.glob('*/index.html'),*ROOT.glob('*/*/index.html')])
    counts=Counter()
    for path in pages:
        source=path.read_text();clean=BLOCK.sub('',source)
        assert not re.search(r'<script[^>]*application/ld\+json',clean,re.I), f'Unmanaged JSON-LD: {path}'
        data=validate(graph(clean))
        payload=json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')
        block='<script type="application/ld+json" id="site-structured-data">'+payload+'</script>'
        updated=clean.replace('</head>',block+'</head>',1)
        if args.check: assert source == updated, f'Stale JSON-LD: {path}'
        elif source != updated:path.write_text(updated)
        counts.update(n['@type'] for n in data['@graph'])
    print(json.dumps({'pages':len(pages),'types':dict(counts),'mode':'check' if args.check else 'write'},ensure_ascii=False))

if __name__ == '__main__':main()
