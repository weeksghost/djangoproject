from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from contact_us.models import ContactForm
from django.template import RequestContext, Context
from django import forms
from django.forms.widgets import *
from django.core.mail import send_mail, BadHeaderError

from django.views.decorators.csrf import csrf_exempt


from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, CreateView, FormView


class CompletedPage(TemplateView):
    template_name = "thankyou.html"

class ContactFormMixin(object):
    """
    Form view that sends email when form is valid. You'll need
    to define your own form_class and template_name.
    """
    def form_valid(self, form):
        form.send_email(self.request)
        return super(ContactFormMixin, self).form_valid(form)

    def get_success_url(self):
        return reverse("contact_us:thankyou")

class send_email():

    def contactview(request):
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        email = request.POST.get('email', '')
    
        recipients = 'erikomarty@gmail.com'
    
        if subject and message and email:
            try:
                send_mail(subject, message, email, recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/thankyou/')
        else:
            form = ContactForm()
            template_name = 'contact_us.html'
        return render(request, template_name, {'form' : form})

class ContactFormView(ContactFormMixin, FormView):
    pass

class ContactModelFormView(ContactFormMixin, CreateView):
    pass




#@csrf_exempt
#def contactview(request):
#
#    if request.method == 'POST':
#        form = ContactForm(request.POST)
#
#        if form.is_valid():
#            subject = form.cleaned_data['subject']
#            message = form.cleaned_data['message']
#            from_email = form.cleaned_data['from_email']
#
#            recipients = ['erikomarty@gmail.com']
#
#            send_mail(subject, message, from_email, recipients)
#            return HttpResponseRedirect('/thankyou/')
#    else:
#        form = ContactForm()
#
#    return render(request, 'contact_us.html', {
#        'form' : form,
#    })
#
#
#def thankyou(request):
#    return render(request, 'thankyou.html', {})
#
#
#def send_email(request):
#    subject = request.POST.get('subject', '')
#    message = request.POST.get('message', '')
#    from_email = request.POST.get('from_email', '')
#    if subject and message and from_email:
#        try:
#            send_mail(subject, message, from_email, ['admin@example.com'])
#        except BadHeaderError:
#            return HttpResponse('Invalid header found.')
#        return HttpResponseRedirect('/contact_us/thankyou/')
#    else:
#        return HttpResponse('Make sure all fields are entered and valid.')


#@csrf_exempt
#def contactview(request):
#
#    if request.method == 'POST':
#        form = ContactForm(request.POST)
#
#        if form.is_valid():
#            subject_id = form.cleaned_data['subject_id']
#            message_id = form.cleaned_data['message_id']
#            from_email_id = form.cleaned_data['from_email_id']
#
#            recipients = ['erikomarty@gmail.com']
#
#            subject = request.POST.get('subject', '')
#            message = request.POST.get('message', '')
#            from_email = request.POST.get('from_email', '')
#            if subject and message and from_email:
#                try:
#                    send_mail(subject, message, from_email, recipients)
#                except BadHeaderError:
#                    return HttpResponse('Invalid header found.')
#                return HttpResponseRedirect('/thankyou/')
#            else:
#                form = ContactForm()
#                template_name = 'contact_us/contact_us.html'
#            #return render(request, template_name, {'form' : form})
#
#
#            return render(request, 'contact_us.html', {
#                'form' : form,
#            })
#
#
#@csrf_exempt
#def thankyou(request):
#    return render(request, 'thankyou.html')


#@csrf_exempt
#def thankyou(request):
#    template_name = 'contact_us/thankyou.html'
#    return render(request, template_name, {})
