from django.urls import path
from .views import (
    IndexView,
    SettingView,
    CustomSignupView,
    social_account_confirmation,
    ProgressView,
    SelectStageView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("accounts/signup/", CustomSignupView.as_view(), name="account_signup"),
    path(
        "accounts/social_confirmation",
        social_account_confirmation,
        name="social_account_confirmation",
    ),
    path("progress_overview", ProgressView.as_view(), name="progress_overview"),
    path("select_stage", SelectStageView.as_view(), name="select_stage"),
    path("setting", SettingView.as_view(), name="setting"),
]
