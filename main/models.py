from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=20, unique=True, verbose_name="ユーザー名", blank=False, null=False
    )
    email = models.EmailField(
        unique=True, verbose_name="メールアドレス", blank=False, null=False
    )

    class Meta:
        verbose_name = "User"


class Stage(models.Model):
    stage_name = models.CharField(
        blank=False, null=False, max_length=20, verbose_name="ステージ名", unique=True
    )
    questions = models.ManyToManyField("Question", verbose_name="問題", blank=True)
    completed_users = models.ManyToManyField(
        "CustomUser", verbose_name="ユーザー", blank=True
    )
    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE, related_name="children"
    )

    def __str__(self):
        return self.stage_name


class Question(models.Model):
    question_name = models.CharField(
        blank=False, null=False, max_length=20, verbose_name="問題名", unique=True
    )
    content = models.TextField(blank=False, null=False, verbose_name="問題文")
    answer = models.TextField(blank=False, null=False, verbose_name="解答")
    completed_users = models.ManyToManyField(
        "CustomUser", verbose_name="ユーザー", blank=True
    )

    def __str__(self):
        return self.question_name
