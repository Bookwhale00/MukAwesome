from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path("api/sign-up/", views.sign_up_view, name="sign-up"),
    path("api/sign-in/", views.sign_in_view, name="sign-in"),
    path("api/logout/", views.logout, name="logout"),
]