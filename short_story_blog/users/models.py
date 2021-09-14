from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .servises import gen_password
from .tasks import send_verification_email

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    confirmed = models.BooleanField()
    code = models.TextField()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Создание модели Profile и отправка кода подтверждения на почту"""
    if created:
        ver_code = gen_password()
        send_verification_email.delay(instance.pk, ver_code)
        Profile.objects.create(user=instance, confirmed=False, code=ver_code)
