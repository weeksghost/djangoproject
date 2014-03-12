from django.db import models
from django import forms
from django.forms.widgets import *
from django.core.mail import send_mail, BadHeaderError


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    body = forms.CharField(widget=Textarea())
