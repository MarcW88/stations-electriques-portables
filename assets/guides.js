(() => {
  const menu = document.querySelector('#guide-navigation');
  const button = document.querySelector('.burger');
  const mobile = window.matchMedia('(max-width: 768px)');
  if (menu && button) {
    const close = (restoreFocus = false) => {
      menu.dataset.open = 'false';
      button.setAttribute('aria-expanded', 'false');
      button.setAttribute('aria-label', 'Ouvrir le menu');
      if (restoreFocus) button.focus();
    };
    button.addEventListener('click', () => {
      const open = button.getAttribute('aria-expanded') !== 'true';
      menu.dataset.open = String(open);
      button.setAttribute('aria-expanded', String(open));
      button.setAttribute('aria-label', open ? 'Fermer le menu' : 'Ouvrir le menu');
      if (open) menu.querySelector('a')?.focus();
    });
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && button.getAttribute('aria-expanded') === 'true') close(true);
    });
    document.addEventListener('click', (event) => {
      if (!event.target.closest('.site-header')) close();
    });
    menu.addEventListener('click', (event) => {
      if (event.target.closest('a')) close();
    });
    mobile.addEventListener('change', () => close());
  }
  document.querySelectorAll('.table-wrap').forEach((wrapper) => {
    wrapper.tabIndex = 0;
    wrapper.setAttribute('role', 'region');
    wrapper.setAttribute('aria-label', 'Tableau comparatif — défilement horizontal');
  });
})();

(()=>{const footer=document.querySelector('footer.site-footer');if(!footer||footer.dataset.energyFooter)return;footer.dataset.energyFooter='true';footer.innerHTML=`
<div class="container">
<section class="footer-decision" aria-labelledby="footer-decision-title"><div class="footer-decision-heading"><p class="footer-eyebrow">Le repère énergie</p><h2 id="footer-decision-title">Avant de choisir, vérifiez ces trois chiffres.</h2><p>Une station adaptée n'est pas seulement celle qui affiche le plus de watts. Comprendre ces repères évite un choix trop limité ou surdimensionné.</p></div><div class="footer-metrics"><a href="/guides/watt-ou-watt-heure/" class="footer-metric"><span class="footer-metric-symbol">W</span><span><strong>Puissance</strong><small>Quels appareils peut-elle alimenter en même temps ?</small></span><span aria-hidden="true">↗</span></a><a href="/guides/calculer-capacite-station-electrique/" class="footer-metric"><span class="footer-metric-symbol">Wh</span><span><strong>Capacité</strong><small>Quelle quantité d'énergie est stockée ?</small></span><span aria-hidden="true">↗</span></a><a href="/calculateur-autonomie/" class="footer-metric"><span class="footer-metric-symbol">h</span><span><strong>Autonomie estimée</strong><small>Combien de temps pour vos appareils, pertes comprises ?</small></span><span aria-hidden="true">↗</span></a></div></section>
<div class="footer-paths"><div><span class="footer-path-number">01 / Évaluer</span><h3>Partir de vos besoins</h3><p>Estimez la consommation avant de regarder les modèles.</p><a href="/calculateur-autonomie/">Utiliser le calculateur →</a></div><div><span class="footer-path-number">02 / Comprendre</span><h3>Lire les bons critères</h3><p>Puissance, capacité, cycles et options de recharge.</p><a href="/guides/comment-choisir-station-electrique-portable/">Consulter le guide de choix →</a></div><div><span class="footer-path-number">03 / Comparer</span><h3>Arbitrer les compromis</h3><p>Identifier les limites, pas seulement les points forts.</p><a href="/comparatifs/meilleure-station-electrique-portable/">Explorer les comparatifs →</a></div></div>
<div class="footer-main"><div class="footer-identity"><a class="footer-brand" href="/">Stations Électriques Portables</a><p class="footer-tagline">Un média pour comprendre l'énergie nomade et choisir selon ses usages. Les données constructeur sont distinguées des mesures indépendantes.</p><a class="footer-method-link" href="/methode-de-test/">Découvrir notre méthode →</a></div><nav class="footer-col" aria-label="Explorer"><h4>Explorer</h4><a href="/comparatifs/">Comparatifs</a><a href="/modeles/">Fiches modèles</a><a href="/marques/">Marques</a><a href="/usages/">Usages</a><a href="/solaire/">Recharge solaire</a></nav><nav class="footer-col" aria-label="Apprendre"><h4>Apprendre</h4><a href="/guides/">Guides pratiques</a><a href="/puissance-capacite/">Puissance et capacité</a><a href="/accessoires/">Accessoires</a><a href="/calculateur-autonomie/">Calculateur d'autonomie</a></nav><nav class="footer-col" aria-label="Le site"><h4>Le site</h4><a href="/a-propos/">À propos</a><a href="/methode-de-test/">Notre méthode</a><a href="/transparence-affiliation/">Transparence et affiliation</a><a href="/contact/">Contact</a><a href="/mentions-legales/">Mentions légales</a></nav></div>
<div class="footer-bottom"><span>© 2026 stations-electriques-portables.fr</span><span>Les autonomies sont des estimations, pas des garanties. Certains liens sont affiliés. <a href="/transparence-affiliation/">Notre politique de transparence</a>.</span></div></div>`;})();
