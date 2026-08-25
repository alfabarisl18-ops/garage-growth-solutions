const demoToggle = document.querySelector('.demo-nav-toggle');
const demoMenu = document.querySelector('#demo-menu');
const demoForm = document.querySelector('[data-demo-form]');
const demoStatus = document.querySelector('[data-demo-status]');

document.querySelectorAll('[data-demo-year]').forEach((element) => {
  element.textContent = new Date().getFullYear();
});

if (demoToggle && demoMenu) {
  demoToggle.addEventListener('click', () => {
    const isOpen = demoMenu.classList.toggle('is-open');
    demoToggle.setAttribute('aria-expanded', String(isOpen));
    demoToggle.querySelector('.screen-reader').textContent = isOpen ? 'Close navigation' : 'Open navigation';
  });

  demoMenu.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      demoMenu.classList.remove('is-open');
      demoToggle.setAttribute('aria-expanded', 'false');
      demoToggle.querySelector('.screen-reader').textContent = 'Open navigation';
    });
  });
}

if (demoForm && demoStatus) {
  demoForm.addEventListener('submit', (event) => {
    event.preventDefault();
    demoStatus.textContent = 'Demo complete: a real shop would receive this request. No information was sent or stored.';
  });
}
