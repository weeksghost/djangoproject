from django.template.loader import get_template
from django.template import Context
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from djangoproject.tasks import send_email
from contact_us.forms import ContactForm


@csrf_exempt
def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject'].name
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email_address']
            message = form.cleaned_data['message']
            to_email = form.cleaned_data['subject'].recipient
            template = get_template('email_template.txt')
            context = Context({
                'name': name,
                'message': message,
                'from_email': from_email,
            })
            body = template.render(context)
            send_email.delay(subject, body, 'erikomarty@gmail.com', to_email)
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
