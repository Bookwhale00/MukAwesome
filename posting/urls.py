from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('api/posting/', views.posting_view, name='posting'),
    path('api/posting-detail/<int:id>', views.posting_detail_view, name='posting_detail'),
    path('/api/mypage/<str:username>',views.mypage_view, name='mypage'),

]