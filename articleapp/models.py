from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


# Create your models here.

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True) # on_delete=models.SET_NULL 유저가 탈퇴했을 시에 게시글을 없애지 않고 게시글의 유저만 null로 바꾼다 이때 null=True도 설정해줘야한다
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_created=True, null=True)

    num_like = models.IntegerField(default=0)
