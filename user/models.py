from django.db import models
from django.contrib.auth.models import AbstractUser

class UserInfo(AbstractUser):
    class Meta:
        db_table = "user_info"
        
    bio = models.CharField(max_length=256)