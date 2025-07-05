// Carousel with fade effect
const images = [
    '/static/main/carousel1.jpg',
    '/static/main/carousel2.jpg',
    '/static/main/carousel3.jpg'
];
let idx = 0;
window.addEventListener('DOMContentLoaded', function() {
    const imgEl = document.getElementById('carousel-img');
    const dots = document.querySelectorAll('.carousel-dot');
    function show(idxToShow) {
        idx = idxToShow;
        imgEl.classList.add('fade-out');
        setTimeout(() => {
            imgEl.src = images[idx];
            dots.forEach((dot, i) => {
                dot.style.opacity = (i === idx) ? '1' : '0.7';
                dot.style.background = (i === idx) ? '#2563eb' : '#fff';
            });
            imgEl.classList.remove('fade-out');
            imgEl.classList.add('fade-in');
            setTimeout(() => imgEl.classList.remove('fade-in'), 600);
        }, 400);
    }
    dots.forEach((dot, i) => {
        dot.addEventListener('click', () => show(i));
    });
    setInterval(() => {
        show((idx + 1) % images.length);
    }, 3500);
    show(0);
});
