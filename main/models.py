from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=20, unique=True, verbose_name="ユーザー名", blank=False, null=False
    )
    email = models.EmailField(
        unique=True, verbose_name="メールアドレス", blank=False, null=False
    )
    # icon = models.ImageField(upload_to="user_icons/", null=True, blank=True)

    class Meta:
        verbose_name = "User"

    def __str__(self):
        return self.username
