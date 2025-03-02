from django.urls import path
from .views import IndexView, SettingView, CustomSignupView, social_account_confirmation

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("setting", SettingView.as_view(), name="setting"),
    path("accounts/signup/", CustomSignupView.as_view(), name="account_signup"),
    path(
        "accounts/social_confirmation",
        social_account_confirmation,
        name="social_account_confirmation",
    ),
]
