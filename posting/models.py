from django.db import models
from user.models import UserInfo


# Create your models here.
class PostingModel(models.Model):
    class Meta:
        db_table = "my_posting"

    author = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    thumbnail = models.TextField(default='')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)