from django.contrib import admin

# Register your models here.
from .models import Portfolio, Service, Feedback, CompanyContact, Picture

admin.site.register(Portfolio)
admin.site.register(Service)
admin.site.register(Feedback)
admin.site.register(CompanyContact)
admin.site.register(Picture)
