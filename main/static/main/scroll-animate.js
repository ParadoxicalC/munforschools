/* Auto-apply load-in and transition animations on page load */
document.addEventListener('DOMContentLoaded', () => {
    // Animate nav, footer, hero, and main sections
    document.querySelectorAll('nav, footer, .hero, .main-section').forEach(el => {
        el.classList.add('fade-in-up');
    });

    // Animate all cards and sections with .pop-in or .fade-in-up
    document.querySelectorAll('.card, .about-card, .committee-card, .expertise-card').forEach((el, i) => {
        setTimeout(() => el.classList.add('pop-in'), 120 + i * 80);
    });

    // Animate staggered grids/lists
    document.querySelectorAll('[data-animate-stagger]').forEach(grid => {
        grid.querySelectorAll(':scope > *').forEach((el, i) => {
            setTimeout(() => {
                el.style.opacity = '1';
                el.style.transform = 'none';
            }, 200 + i * 120);
        });
    });
});

// Pop-up animation on scroll for about page cards
document.addEventListener('DOMContentLoaded', () => {
  const cards = document.querySelectorAll('.about-card');
  if (!cards.length) return;
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.18 });
  cards.forEach(card => observer.observe(card));
});

// Pop-up animation on scroll for all text boxes
document.addEventListener('DOMContentLoaded', () => {
  const boxes = document.querySelectorAll('.animated-textbox');
  if (!boxes.length) return;
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });
  boxes.forEach(box => observer.observe(box));
});