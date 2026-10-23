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
