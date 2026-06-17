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


// new added line for test

document.addEventListener("DOMContentLoaded", () => {
  const contactForm = document.querySelector(".contact-form");

  if (!contactForm) {
    return;
  }

  const formMessage = contactForm.querySelector(".form-message");
  const submitButton = contactForm.querySelector('button[type="submit"]');

  contactForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    // Clear any previous message.
    formMessage.textContent = "";
    formMessage.classList.remove("success", "error");

    // Prevent repeated submissions.
    submitButton.disabled = true;
    submitButton.textContent = "Sending...";

    try {
      const response = await fetch(contactForm.action, {
        method: "POST",
        body: new FormData(contactForm),
        headers: {
          Accept: "application/json"
        }
      });

      if (response.ok) {
        formMessage.textContent =
          "Thank you! Your request has been sent successfully. We will contact you soon.";

        formMessage.classList.add("success");

        // Clear the form only after Formspree confirms it was sent.
        contactForm.reset();
      } else {
        const responseData = await response.json();

        if (responseData.errors) {
          formMessage.textContent = responseData.errors
            .map((error) => error.message)
            .join(", ");
        } else {
          formMessage.textContent =
            "Sorry, your request could not be sent. Please try again.";
        }

        formMessage.classList.add("error");
      }
    } catch (error) {
      console.error("Form submission error:", error);

      formMessage.textContent =
        "There was a connection problem. Please check your internet and try again.";

      formMessage.classList.add("error");
    } finally {
      submitButton.disabled = false;
      submitButton.textContent = "Send Request";
    }
  });
});

// form.addEventListener('submit', (event) => {
  // event.preventDefault();
  // formMessage.textContent = 'Thanks — your request is ready to send. Connect this form to your preferred email or CRM service when you deploy.';
  // form.reset();
// });
