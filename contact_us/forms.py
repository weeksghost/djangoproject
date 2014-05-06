from django import forms
from contact_us.models import Contact


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email_address = forms.EmailField()
    subject = forms.ModelChoiceField(queryset=Contact.objects.all(), empty_label=None)
    message = forms.CharField()
