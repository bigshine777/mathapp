from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (
    IndexView,
    SettingView,
    CustomSignupView,
    social_account_confirmation,
    ProgressView,
    SelectStageView,
    StageViewSet,
    StageDetailView,
    QuestionDetailView,
)

router = DefaultRouter()
router.register(r'stages', StageViewSet)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("accounts/signup/", CustomSignupView.as_view(), name="account_signup"),
    path(
        "accounts/social_confirmation",
        social_account_confirmation,
        name="social_account_confirmation",
    ),
    path('api/', include(router.urls)),
    path("progress_overview", ProgressView.as_view(), name="progress_overview"),
    path("stages", SelectStageView.as_view(), name="stages"),
    path("stages/<int:pk>/", StageDetailView.as_view(), name="stage_detail"),
    path("questions/<int:pk>", QuestionDetailView.as_view(), name="question_detail"),
    path("setting", SettingView.as_view(), name="setting"),
]
