from django.urls import resolve
from .models import CompanyContact


def current_url_name(request):
    return {
        'current_url_name': resolve(request.path_info).url_name
    }


def contact_info(request):
    contact_info = CompanyContact.objects.first()
    return {'contact_info': contact_info}
