from django.contrib.auth.models import User
from django.db import models

from articleapp.models import Article


# Create your models here.
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='like')

    class Meta:
        unique_together = ('user', 'article')
