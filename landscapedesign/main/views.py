import logging
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import FeedbackForm
from django.conf import settings
from django.contrib import messages
from .models import Service, Portfolio

logger = logging.getLogger(__name__)


def home(request):
    # top_main_picture = PagePicture.objects.filter(location='top_main')
    # middle_main_picture = PagePicture.objects.filter(location='middle_main').first()
    highlighted_services = Service.objects.filter(highlight_on_main=True)[:3]
    highlighted_portfolio = Portfolio.objects.filter(highlight_on_main=True)[:6]

    context = {
        # 'top_main_picture': top_main_picture,
        # 'middle_main_picture': middle_main_picture,
        'highlighted_services': highlighted_services,
        'highlighted_portfolio': highlighted_portfolio,
    }
    return render(request, 'index.html', context)


def about(request):
    # about_us_picture = PagePicture.objects.filter(location='about_us').first()
    context = {
        # 'about_us_picture': about_us_picture,
    }
    return render(request, 'about.html', context)


def services(request):
    # services_top_picture = PagePicture.objects.filter(location='services_top').first()
    services = Service.objects.all()
    context = {
        # 'services_top_picture': services_top_picture,
        'services': services,
    }
    return render(request, 'services.html', context)


def portfolio(request):
    portfolio_items = Portfolio.objects.all()
    context = {
        'portfolio_items': portfolio_items,
    }
    return render(request, 'portfolio.html', context)


def place_order(request):
    success_message = None  # Initialize success message
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save()  # Save the new contact submission to the database

            # Prepare email content
            subject = 'New Feedback Submission'
            message = f"""
                        New feedback submission from {feedback.name}.

                        Phone: {feedback.phone}
                        Email: {feedback.email}
                        Message:
                        {feedback.message}
                        """
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.DEFAULT_FROM_EMAIL]  # Send to the admin's email

            # Send email
            try:
                send_mail(subject, message, from_email, recipient_list)
                success_message = 'Ваше сообщение было успешно отправлено. Мы свяжемся с вами в ближайшее время.'
                form = FeedbackForm()  # Reset the form after saving
            except Exception as e:
                # Log the detailed error
                logger.error(f'Error sending email: {str(e)}')
                # Add a user-friendly error message
                messages.error(request,
                               'Произошла ошибка при отправке сообщения.'
                               ' Пожалуйста, попробуйте еще раз позже.')
    else:
        form = FeedbackForm()

    return render(request, 'place_order.html', {'form': form, 'success_message': success_message})


def custom_404(request, exception):
    return render(request, '404.html', {}, status=404)


# Blog pages; Not used so far
'''def blog_home_1(request):
    return render(request, 'blog-home-1.html')

def blog_home_2(request):
    return render(request, 'blog-home-2.html')

def blog_post(request):
    return render(request, 'blog-post.html')'''

"""
def faq(request):
    return render(request, 'faq.html')"""

# Other portfolio options
"""def portfolio_2_col(request):
    return render(request, 'portfolio-2-col.html')

def portfolio_3_col(request):
    return render(request, 'portfolio-3-col.html')

def portfolio_4_col(request):
    return render(request, 'portfolio-4-col.html')

def portfolio_item(request):
    return render(request, 'portfolio-item.html')"""


# Not used so far
'''def pricing(request):
    return render(request, 'pricing.html')'''
