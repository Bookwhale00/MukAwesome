from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
<<<<<<< HEAD
    path("sign-up/", views.sign_up_view, name="sign-up"),
    path("sign-in/", views.sign_in_view, name="sign-in"),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.profile_view, name="profile"),
]
=======
    path("api/sign-up/", views.sign_up_view, name="sign-up"),
    path("api/sign-in/", views.sign_in_view, name="sign-in"),
    path("api/logout/", views.logout, name="logout"),
]
>>>>>>> 095bdc35c36bea9b830b09c2b232276478854d22
