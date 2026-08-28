const navToggle = document.querySelector('.nav-toggle');
const navMenu = document.querySelector('#nav-menu');

document.querySelectorAll('[data-current-year]').forEach((element) => {
  element.textContent = new Date().getFullYear();
});

if (navToggle && navMenu) {
  navToggle.addEventListener('click', () => {
    const isOpen = navMenu.classList.toggle('is-open');
    navToggle.setAttribute('aria-expanded', String(isOpen));
    navToggle.querySelector('.sr-only').textContent = isOpen ? 'Close navigation' : 'Open navigation';
  });

  navMenu.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      navMenu.classList.remove('is-open');
      navToggle.setAttribute('aria-expanded', 'false');
      navToggle.querySelector('.sr-only').textContent = 'Open navigation';
    });
  });
}

document.querySelectorAll('[data-contact-form]').forEach((contactForm) => {
  const formStatus = contactForm.querySelector('[data-form-status]');

  if (!formStatus) return;

  contactForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const submitButton = contactForm.querySelector('button[type="submit"]');
    const originalButtonContent = submitButton.innerHTML;
    submitButton.disabled = true;
    submitButton.textContent = 'Sending your request…';
    formStatus.className = 'form-status';
    formStatus.textContent = '';

    try {
      const response = await fetch(contactForm.action, {
        method: 'POST',
        body: new FormData(contactForm),
        headers: { Accept: 'application/json' }
      });

      if (!response.ok) {
        throw new Error('Form submission failed');
      }

      contactForm.reset();
      formStatus.classList.add('is-success');
      formStatus.textContent = contactForm.dataset.successMessage || 'Your request was sent. Alpha will follow up with the next step.';
    } catch (error) {
      formStatus.classList.add('is-error');
      formStatus.textContent = 'Your request could not be sent. Please check your connection and try again.';
    } finally {
      submitButton.disabled = false;
      submitButton.innerHTML = originalButtonContent;
    }
  });
});
