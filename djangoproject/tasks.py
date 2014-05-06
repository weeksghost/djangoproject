import celery

from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.defaultfilters import striptags
from smtplib import SMTPDataError


@celery.task
def send_email(subject, body, from_email, to_email, html=False):
    try:
        if html:
            text_body = striptags(body)
            message = EmailMultiAlternatives(subject,
                                             text_body,
                                             from_email,
                                             [to_email])
            message.attach_alternative(body, "text/html")
            message.send()
        else:
            send_mail(subject, body, from_email, [to_email])
    except SMTPDataError as e:
        admins = getattr(settings, 'ADMINS')
        if admins:
            error_to_emails = [email for name, email in admins]
            error_subject = '[DjangoProject] send_email Task Error'
            error_from_email = 'erikomarty@gmail.com'
            error_template = """
                Django Project CMS failed to send the following email

                ERROR:   %s - %s

                TO:      %s
                FROM:    %s
                SUBJECT: %s

                CONTENT:

                %s
            """
            error_body = error_template % (e.smtp_code,
                                           e.smtp_error,
                                           from_email,
                                           to_email,
                                           subject,
                                           body)
            send_mail(error_subject,
                      error_body,
                      error_from_email,
                      error_to_emails)
        else:
            raise e
    except Exception as exc:
        send_email.retry(exc=exc)
