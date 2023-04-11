from django.db import models
from user.models import UserInfo


# Create your models here.
class PostingModel(models.Model):
    class Meta:
        db_table = "my_posting"

    img = "../templates/img/thumbnail.png"

    # user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    author = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    thumbnail = models.CharField(max_length=256, default=img)
    content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)