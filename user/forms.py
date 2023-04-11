from django.contrib.auth.forms import UserChangeForm
from .models import UserInfo

# 프로필 수정 ( UserInfo 수정 )
class UpdateUserInfo(UserChangeForm):
    class Meta:
        model = UserInfo
        fields = ('username', 'email', 'bio', 'tmi', 'mbti', 'favorite')