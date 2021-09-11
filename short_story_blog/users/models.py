from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail


from .servises import gen_password
User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    confirmed = models.BooleanField()
    code = models.TextField()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ver_code = gen_password()
        send_mail('password',f'uoyr code {ver_code}', 'from@example.com',(instance.email,))

        Profile.objects.create(user=instance,confirmed=False, code=ver_code)
