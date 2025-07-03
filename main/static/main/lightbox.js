// Minimal lightbox functionality for gallery images
// You can replace this with a library like baguetteBox.js for a better experience

document.addEventListener('DOMContentLoaded', function () {
    const links = document.querySelectorAll('a[data-lightbox]');
    links.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const img = document.createElement('img');
            img.src = this.href;
            img.style.maxWidth = '90vw';
            img.style.maxHeight = '90vh';
            img.style.display = 'block';
            img.style.margin = '5vh auto';
            const overlay = document.createElement('div');
            overlay.style.position = 'fixed';
            overlay.style.top = 0;
            overlay.style.left = 0;
            overlay.style.width = '100vw';
            overlay.style.height = '100vh';
            overlay.style.background = 'rgba(0,0,0,0.8)';
            overlay.style.zIndex = 1000;
            overlay.appendChild(img);
            overlay.addEventListener('click', function () {
                document.body.removeChild(overlay);
            });
            document.body.appendChild(overlay);
        });
    });
});
