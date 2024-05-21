import logging
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import FeedbackForm
from django.conf import settings
from django.contrib import messages

logger = logging.getLogger(__name__)


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def portfolio(request):
    return render(request, 'portfolio.html')


# def contacts(request):
#     return render(request, 'contacts.html')


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
                               'Произошла ошибка при отправке сообщения. Пожалуйста, попробуйте еще раз позже.')
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
