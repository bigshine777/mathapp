from rest_framework import serializers
from .models import CustomUser, Stage, Question


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'content', 'answer']


class StageSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    completed_users = CustomUserSerializer(many=True, read_only=True)
    children = serializers.SerializerMethodField()

    class Meta:
        model = Stage
        fields = ['id', 'stage_name', 'questions', 'completed_users', 'parent', 'children']

    def get_children(self, obj):
        return StageSerializer(obj.children.all(), many=True).data
