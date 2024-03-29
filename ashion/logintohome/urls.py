from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("otpverify/<str:id>/", views.otp_verification, name="otpverify"),
    path("contact/", views.contact, name="contact"),
]
