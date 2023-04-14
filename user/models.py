from django.db import models
from django.contrib.auth.models import AbstractUser

class UserInfo(AbstractUser):
    class Meta:
        db_table = "user_info"

    bio = models.CharField(blank=True, max_length=256, default='')
    tmi = models.CharField(blank=True, max_length=256, default='')
    mbti = models.CharField(blank=True, max_length=256, default='')
    favorite = models.CharField(blank=True, max_length=256, default='')
    # img = models.TextField(default='')
    img = models.URLField(blank=True, null=True, default='')
    # 한마디, tmi, mbti, 좋아하는 음식 필드 추가
    