from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from config.settings import DEFAULT_FROM_EMAIL
import time
from datetime import datetime
from app_accounts.models import User
from app_accounts.tokens import activate_token

from django.conf import settings


def task_send_register_mail(user, domain):
    try:

        template = 'mail_register.html'
        now_time = time.mktime(datetime.now().timetuple())

        kwargs = {
            'uid': urlsafe_base64_encode(force_bytes(user.id)),
            'token': activate_token.make_token(user),
            'time': int(now_time)
        }
        message = render_to_string(template, {
            'user': user,
            'domain': domain,
            'kwargs' : kwargs,
        })
        mail_subject = '회원가입 인증메일'
        to_email = [user.email]
        from_email = DEFAULT_FROM_EMAIL
        body = ''
        email = EmailMultiAlternatives(mail_subject, body, from_email, to_email)
        email.attach_alternative(message, "text/html")
        email.send()

    except User.DoesNotExist as e:
        print('email send error')