from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('committees/', views.committees, name='committees'),
    path('committees/<int:pk>/', views.committee_detail, name='committee_detail'),
    path('itinerary/', views.itinerary, name='itinerary'),
    path('gallery/', views.gallery, name='gallery'),
    path('resources/', views.resources, name='resources'),
]
