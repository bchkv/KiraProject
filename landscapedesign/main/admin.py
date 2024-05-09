from django.contrib import admin

# Register your models here.
from .models import Project, Service, Feedback, GalleryImage

admin.site.register(Project)
admin.site.register(Service)
admin.site.register(Feedback)
admin.site.register(GalleryImage)
