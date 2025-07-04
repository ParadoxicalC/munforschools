from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .models import (
    SecretariatMember, ExecutiveBoardMember, Committee, ItineraryEvent,
    GalleryImage, ResourceLink
)
from .forms import SignupForm

def home(request):
    return render(request, 'main/home.html')

def about(request):
    secretariat = SecretariatMember.objects.all()
    eboard = ExecutiveBoardMember.objects.all()
    return render(request, 'main/about.html', {
        'secretariat': secretariat,
        'eboard': eboard,
    })

def committees(request):
    committees = Committee.objects.all()
    return render(request, 'main/committees.html', {'committees': committees})

def committee_detail(request, pk):
    committee = get_object_or_404(Committee, pk=pk)
    return render(request, 'main/committee_detail.html', {'committee': committee})

def itinerary(request):
    days = {1: [], 2: [],}
    for event in ItineraryEvent.objects.all():
        days[event.day].append(event)
    return render(request, 'main/itinerary.html', {'days': days})

def gallery(request):
    chapter1 = GalleryImage.objects.filter(chapter=1)
    chapter2 = GalleryImage.objects.filter(chapter=2)
    return render(request, 'main/gallery.html', {
        'chapter1': chapter1,
        'chapter2': chapter2,
    })

def resources(request):
    links = ResourceLink.objects.all()
    form = SignupForm()
    message = None
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signup = form.save()
            # Send welcome email
            send_mail(
                subject="Welcome to MUN4Schools!",
                message=render(request, 'main/email_welcome.txt', {'signup': signup}).content.decode(),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[signup.email],
                fail_silently=False,
            )
            message = "Thank you for signing up! Please check your email."
            form = SignupForm()  # reset form
    return render(request, 'main/resources.html', {
        'links': links,
        'form': form,
        'message': message,
    })
