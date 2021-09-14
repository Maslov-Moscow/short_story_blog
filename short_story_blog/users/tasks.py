import logging

from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model

from celery import shared_task


@shared_task
def send_verification_email(user_id, ver_code):
    """Отправка письма с кодом"""
    User = get_user_model()
    logging.info(f"Отправка письма для  {user_id}")
    try:
        user = User.objects.get(id=user_id)
        if not settings.DEBUG:
            send_mail('password', f'Ваш код подтверждения {ver_code}', settings.EMAIL_HOST_USER, (user.email,))
        else:
            send_mail('password', f'Ваш код подтверждения {ver_code}', 'test@test.com', (user.email,))
        return None
    except Exception as ex:
        logging.warning(f"{ex}")
