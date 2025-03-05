from django.contrib import admin
from .models import CustomUser, Stage, Question

admin.site.register(CustomUser)

@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    filter_horizontal = ('questions', 'completed_users')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    filter_horizontal = ('completed_users',)
