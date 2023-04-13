from django.urls import path
from . import views

urlpatterns = [

    path('', views.home_view, name='home'), # 127.0.0.1:8000 과 views.py 폴더의 home 함수 연결
    path('api/posting/', views.posting_view, name='posting'),
    path('api/posting-detail/<int:id>', views.posting_detail_view, name='posting_detail'),
    path('api/mypage/<str:username>', views.mypage_list_view, name='mypage'),
    path('api/mypage/edit/<int:pk>', views.mypage_edit_view, name='posting_edit'),
]

