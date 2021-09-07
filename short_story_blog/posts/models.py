from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField(verbose_name="Текст ")
    pub_date = models.DateTimeField( auto_now_add=True)
    score = models.IntegerField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.text[:15]