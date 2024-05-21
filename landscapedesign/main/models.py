from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

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


class GalleryImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery_images/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
