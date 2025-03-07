from django.shortcuts import redirect
from django.contrib import messages
from .models import Question

class QuestionAccessMixin:
    """
    このMixinを適用したビューでは、前の問題を解いていない場合や
    ステージをクリアしていない場合にアクセス制限を行う。
    """

    def dispatch(self, request, *args, **kwargs):
        question = self.get_object()
        
        if (question.stage.parent and not (request.user in question.stage.parent.completed_users.all())):
            messages.error(request, "問題にアクセスするにはこのステージをクリアしてください")
            return redirect("stage_detail", pk=question.stage.parent.id)

        previous_question = Question.objects.filter(
            stage=question.stage, question_number=question.question_number - 1
        ).first()
        
        if previous_question and request.user not in previous_question.completed_users.all():
            messages.error(request, "前の問題を解いてから進んでください。")
            return redirect("stage_detail", pk=question.stage.id)

        return super().dispatch(request, *args, **kwargs)

class StageAccessMixin:
    """
    このMixinを適用したビューでは、ステージをクリアしていない場合にアクセス制限を行う。
    """

    def dispatch(self, request, *args, **kwargs):
        stage = self.get_object()
        print(stage)
        
        if (stage.parent and not (request.user in stage.parent.completed_users.all())):
            messages.error(request, "このステージを先にクリアしてください")
            return redirect("stage_detail", pk=stage.parent.id)

        return super().dispatch(request, *args, **kwargs)
