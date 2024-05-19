from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'phone', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full Name',
                'id': 'name',
                'required': 'required',
                'data-validation-required-message': "Please enter your name."
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number',
                'id': 'phone',
                'required': 'required',
                'data-validation-required-message': "Please enter your phone number."
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address',
                'id': 'email',
                'required': 'required',
                'data-validation-required-message': "Please enter your email address."
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message',
                'id': 'message',
                'required': 'required',
                'data-validation-required-message': "Please enter your message",
                'rows': 5,
                'cols': 100,
                'style': 'resize:none;'
            }),
        }

