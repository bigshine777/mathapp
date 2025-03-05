# Generated by Django 5.1.6 on 2025-03-04 02:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_question_completed"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="question",
            name="completed",
        ),
        migrations.RemoveField(
            model_name="stage",
            name="completed",
        ),
        migrations.AlterField(
            model_name="question",
            name="question_name",
            field=models.CharField(max_length=20, unique=True, verbose_name="問題名"),
        ),
        migrations.AlterField(
            model_name="stage",
            name="stage_name",
            field=models.CharField(
                max_length=20, unique=True, verbose_name="ステージ名"
            ),
        ),
        migrations.CreateModel(
            name="UserQuestionProgress",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("completed", models.BooleanField(default=False)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.question"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserStageProgress",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("completed", models.BooleanField(default=False)),
                (
                    "stage",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.stage"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
