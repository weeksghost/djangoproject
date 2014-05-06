from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from djangoproject.tasks import send_email
from contact_us.forms import ContactForm


@csrf_exempt
def contact_form(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email_address']
            message = form.cleaned_data['message']
            to_email = form.cleaned_data['subject'].recipient
            subject = "Contact Request Received"
            template = get_template('email_template.txt')
            context = Context({
                'name': name,
                'message': message,
                'from_email': from_email,
            })
            body = template.render(context)
            send_email.delay(subject, body, from_email, 'erikomarty@gmail.com')
            url = reverse('thankyou', args=())
            return redirect(url)
    else:
        form = ContactForm()
    template_name = 'contact_us.html'
    context = {'form': form}
    return render(request, template_name, context)


def thankyou(request):
    template_name = 'thankyou.html'
    return render(request, template_name, {})
