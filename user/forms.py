from django.contrib.auth.forms import UserChangeForm
from .models import UserInfo
from django import forms 
from django.core.validators import validate_email

# MBTI_CHOICES = (
#     ('ISTJ', 'ISTJ'),
#     ('ISTP', 'ISTP'),
#     ('INFJ', 'INFJ'),
#     ('INTJ', 'INTJ'),
#     ('ISFJ', 'ISFJ'),
#     ('ISFP', 'ISFP'),
#     ('INFP', 'INFP'),
#     ('INTP', 'ISTJ'),
#     ('ESTJ', 'ESTJ'),
#     ('ESFP', 'ESFP'),
#     ('ENFP', 'ENFP'),
#     ('ENTP', 'ENTP'),
#     ('ESFJ', 'ESFJ'), 
#     ('ENFJ', 'ENFJ'),
#     ('ENTJ', 'ENTJ'),
# )

# 프로필 수정 ( UserInfo 수정 )
class UpdateUserInfo(UserChangeForm):
    # 이메일 유효성 검사 (주소 형식과 DNS검사)
    email = forms.EmailField(validators=[validate_email])

    # mbti 16개 중에서 선택
    # mbti = forms.ChoiceField(choices=MBTI_CHOICES)

    class Meta:
        model = UserInfo
        fields = ('username', 'email', 'bio', 'tmi', 'mbti', 'favorite')