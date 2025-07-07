# MUN4Schools Chapter 2 (2025) Website

A modern, production-ready Django website for MUN4Schools, fully manageable via Django admin.

## Features

- Modern, responsive design (Tailwind CSS)
- Sticky navbar, logo, and elegant layout
- Home, About, Committees, Itinerary, Gallery, Resources pages
- All content managed via Django admin (Secretariat, EB, Committees, Gallery, Itinerary, Resources)
- Signup form with real email sending
- Gallery with lightbox, image uploads, and year categorization
- SEO-ready, mobile-friendly

## Setup (for Developers)

1. **Clone the repo**  
   `git clone ...`
2. **Install Python dependencies like Django and Pillow**  
   Use `pip install` commands  to Install django and Pillow
3. **Install Node.js dependencies for Tailwind**  
   `npm install`
4. **Build Tailwind CSS**  
   `npm run build:css`
5. **Configure `.env` or `settings.py` for email and secret key**
6. **Run migrations**  
   `python manage.py migrate`
7. **Create superuser**  
   `python manage.py createsuperuser`
8. **Run the server**  
   `python manage.py runserver`
9. **Access admin**  
   `http://localhost:8000/admin/`

## Setup (for Non-Tech Admins)

- Log in to `/admin/` with your credentials.
- Add/edit Secretariat, Executive Board, Committees, Committee Members, Itinerary Events, Gallery Images, and Resource Links.
- Upload images and background guides as needed.
- All content updates are live on the site.

## Deployment

- Ready for Heroku, Render, or any Django-compatible host.
- Set `DEBUG=False` and configure allowed hosts, static/media storage, and email backend for production.

---

**You now have a complete, production-ready, fully manageable MUN4Schools website!**
