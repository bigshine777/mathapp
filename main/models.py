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
    completed_users = models.ManyToManyField(
        "CustomUser", verbose_name="ユーザー", blank=True
    )
    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE, related_name="children"
    )

    def __str__(self):
        return self.stage_name

    @property
    def first_question(self):
        return self.questions.filter(question_number=1).first()

    def completed_count(self, user):
        return self.questions.filter(completed_users=user).count()


QUESTION_TYPES = [
    ("simple_number", "単一数字"),
    ("single_addition", "一桁の足し算"),
    ("static_question", "固定問題"),
]


class Question(models.Model):
    stage = models.ForeignKey(
        "Stage",
        on_delete=models.CASCADE,
        related_name="questions",
        null=False,
        blank=False,
    )
    question_number = models.IntegerField(default=1, null=False, blank=False)
    question_type = models.CharField(
        max_length=50,
        choices=QUESTION_TYPES,
        default="simple_number",
        verbose_name="問題の種類",
    )
    content = models.TextField(blank=False, null=False, verbose_name="問題文")
    answer = models.TextField(blank=False, null=False, verbose_name="解答")
    completed_users = models.ManyToManyField(
        "CustomUser", verbose_name="ユーザー", blank=True
    )

    def __str__(self):
        return self.stage.stage_name + "-" + str(self.question_number)

    @property
    def next_question(self):
        return Question.objects.filter(
            stage=self.stage, question_number=self.question_number + 1
        ).first()

    @property
    def last_question(self):
        return Question.objects.filter(
            stage=self.stage, question_number=self.question_number - 1
        ).first()
