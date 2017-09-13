from django.conf import settings
from django.core import mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def email_send(subject, template, recipients, context, default_from=None):
    msg_html = render_to_string(template, context)
    if not default_from:
        default_from = getattr(settings, 'DEFAULT_FROM_EMAIL', '')
    template_email_text = ''
    email = EmailMultiAlternatives(subject=subject, body=template_email_text,
                                   from_email=default_from,
                                   to=recipients, reply_to=[''],
                                   alternatives=((msg_html, 'text/html'),))
    return email.send(fail_silently=True)


def bulk_mail_send(subject, template, recipients_list, context):
    msg_html = render_to_string(template, context)
    default_from = getattr(settings, 'DEFAULT_FROM_EMAIL', '')
    template_email_text = ''
    connection = mail.get_connection()
    connection.open()
    email = EmailMultiAlternatives(subject=subject, body=template_email_text,
                                   from_email=default_from, to=recipients_list,
                                   connection=connection, reply_to=[''],
                                   alternatives=((msg_html, 'text/html'),))
    email.send(fail_silently=True)
    connection.close()
    return True
