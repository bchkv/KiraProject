from django.shortcuts import render
from .models import Project, Service, GalleryImage, Feedback
from .forms import FeedbackForm
from django.http import HttpResponseRedirect


# Displays a list of projects, generates the main page based on the Project model and home.html template
def home(request):
    projects = Project.objects.all()
    return render(request, 'main/home.html', {'projects': projects})


# Retrieves all services from the Service model and passes them to the services.html template
def services(request):
    services = Service.objects.all()
    return render(request, 'main/services.html', {'services': services})


# Fetches all images from the GalleryImage model and passes them to the gallery.html template
def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'main/gallery.html', {'images': images})


# Simply renders the about_us.html template. This page typically contains static information about your company.
def about_us(request):
    return render(request, 'main/about_us.html')


# Handles the feedback form
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        # If the form is submitted and valid, it saves the feedback and redirects to a thank you page
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = FeedbackForm()
    return render(request, 'main/feedback.html', {'form': form})


# Renders a simple thank you page after a user submits the feedback form
def thanks(request):
    return render(request, 'main/thanks.html')