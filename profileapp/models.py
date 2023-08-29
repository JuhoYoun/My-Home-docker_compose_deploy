from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    # One to One Matching 이 프로파일의 주인이 누구인가
    # OneToOneField 는 장고에서 제공해주는 필드로 User 객체와 1대1 매칭을 하고 on_delete=models.CASCADE 이 부분은 해당 User 객체가
    # 삭제 되었을 때 Profile 객체도 같이 삭제된다는 의미이다.
    # related_name='profile' 이 부분은 profile 객체를 user 객체의 attribute 처럼 쓸 수 있게 연결해준다.
    # request.user.profile.nickname 이런식으로 사용 가능하다
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # media root 가 BASE_DIR/media이므로 image는 BASE_DIR/media/profile 에 저장되고 이 필드는 null이 가능하다
    image = models.ImageField(upload_to='profile/', null=True)
    # Profile 객체들의 nickname 은 unique 해야하고 원래 이부분은 null=False 인게 맞는거같은데 가입할 때 nickname 만들라고 안헸으니 True 로 해놓고 나중에 만들라하자
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)
