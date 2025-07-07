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