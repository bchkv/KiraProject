from django.contrib import admin

# Register your models here.
from .models import Project, Service, Feedback

admin.site.register(Project)
admin.site.register(Service)
admin.site.register(Feedback)
