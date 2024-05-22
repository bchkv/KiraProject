from django.db import models


class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/')
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    highlight_on_main = models.BooleanField(default=False)  # Field to indicate if the service should be highlighted
    # on the main page

    def __str__(self):
        return self.title


class Service(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    description = models.TextField()
    highlight_on_main = models.BooleanField(default=False)  # Field to indicate if the service should be highlighted
    # on the main page

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name='Full Name')
    phone = models.CharField(max_length=20, verbose_name='Phone Number')
    email = models.EmailField(verbose_name='Email Address')
    message = models.TextField(verbose_name='Message')
    date_submitted = models.DateTimeField(auto_now_add=True, verbose_name='Date Submitted')  # Automatically set the
    # date when the form is submitted

    def __str__(self):
        return (f"Feedback from {self.name} on {self.date_submitted.strftime('%Y-%m-%d')} at"
                f" {self.date_submitted.strftime('%H:%M:%S')}")


class CompanyContact(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    working_hours = models.CharField(max_length=255)
    telegram = models.URLField(blank=True)
    whatsapp = models.URLField(blank=True)

    def __str__(self):
        return f"Contact Information: {self.address}"
