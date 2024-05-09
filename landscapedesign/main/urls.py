from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('about-us/', views.about_us, name='about_us'),
    path('feedback/', views.feedback, name='feedback'),
    path('thanks/', views.thanks, name='thanks'),
]
