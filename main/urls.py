from django.urls import path
from .views import IndexView, SettingView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("setting", SettingView.as_view(), name="setting"),
]
