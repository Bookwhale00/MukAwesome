from django.contrib.auth.forms import UserChangeForm
from .models import UserInfo
from django import forms 
from django.core.validators import validate_email

# 프로필 수정 ( UserInfo 수정 )
class UpdateUserInfo(UserChangeForm):
    # 이메일 유효성 검사 (주소 형식과 DNS검사)
    email = forms.EmailField(validators=[validate_email])

    class Meta:
        model = UserInfo
        fields = ('img','username', 'email', 'bio', 'tmi', 'mbti', 'favorite')
