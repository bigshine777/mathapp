import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mathapp.settings")
django.setup()

from main.models import Stage, Question

for stage in Stage.objects.all():
    stage.completed_users.clear()

for question in Question.objects.all():
    question.completed_users.clear()

print("completed_users をクリアしました。")
