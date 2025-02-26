from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("main.urls")),  # "main" アプリの URL を読み込む
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),  # Django 管理画面
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
