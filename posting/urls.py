from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'), # 127.0.0.1:8000 과 views.py 폴더의 home 함수 연결
    path('api/posting/', views.posting_view, name='posting'), # 127.0.0.1:8000/tweet 과 views.py 폴더의 tweet 함수 연결
    path('api/mypage/<int:id>', views.mypage_list_view, name='mypage'),
]