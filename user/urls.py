from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path("sign-up/", views.sign_up_view, name="sign-up"),
    path("sign-in/", views.sign_in_view, name="sign-in"),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.profile_view, name="profile"),
]
