from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path("api/sign-up/", views.sign_up_view, name="sign-up"),
    path("api/sign-in/", views.sign_in_view, name="sign-in"),
    path("api/logout/", views.logout, name="logout"),
    path("api/profile/", views.profile_view, name="profile"),
    path("api/profile/update/", views.profile_update_view, name="profile-update"),
    path("api/delete-user/", views.delete_user_view, name='delete-user')
]
