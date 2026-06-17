const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('#navLinks');
const serviceSelect = document.querySelector('#serviceNeeded');
const form = document.querySelector('.contact-form');
const formMessage = document.querySelector('.form-message');

document.querySelector('#year').textContent = new Date().getFullYear();

navToggle.addEventListener('click', () => {
  const isOpen = navLinks.classList.toggle('open');
  navToggle.setAttribute('aria-expanded', String(isOpen));
});

navLinks.querySelectorAll('a').forEach((link) => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('open');
    navToggle.setAttribute('aria-expanded', 'false');
  });
});

document.querySelectorAll('[data-service]').forEach((button) => {
  button.addEventListener('click', () => {
    if (serviceSelect) {
      serviceSelect.value = button.dataset.service;
    }
  });
});

// form.addEventListener('submit', (event) => {
  // event.preventDefault();
  // formMessage.textContent = 'Thanks — your request is ready to send. Connect this form to your preferred email or CRM service when you deploy.';
  // form.reset();
// });
