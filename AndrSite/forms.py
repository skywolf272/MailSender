from django import forms
from .models import MailSender

class UserForm(forms.form):
    class Meta:
        model = MailSender
        model.MailTo = forms.CharField()
        model.MailText = forms.TextField()