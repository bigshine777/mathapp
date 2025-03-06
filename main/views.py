from django.views.generic import TemplateView, ListView, DetailView
from allauth.account.views import SignupView
from .forms import CustomSignupForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from allauth.socialaccount.models import SocialAccount
from .models import CustomUser, Stage, Question
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets
from .serializers import StageSerializer


class IndexView(TemplateView):
    template_name = "main/index.html"


class CustomSignupView(SignupView):
    form_class = CustomSignupForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs


class ProgressView(LoginRequiredMixin, TemplateView):
    template_name = "main/progress_overview.html"

    def get_context_data(self, **kwargs):
        total_stages = Stage.objects.all().count()
        completed_stages = Stage.objects.filter(
            completed_users=self.request.user
        ).count()
        stages_percentage = int(
            (completed_stages / total_stages * 100) if total_stages > 0 else 0
        )

        total_questions = Question.objects.all().count()
        completed_questions = Question.objects.filter(
            completed_users=self.request.user
        ).count()
        questions_percentage = int(
            (completed_questions / total_questions * 100) if total_questions > 0 else 0
        )

        context = {
            "stages_percentage": stages_percentage,
            "questions_percentage": questions_percentage,
        }
        return context


class SelectStageView(LoginRequiredMixin, ListView):
    template_name = "main/select_stage.html"
    model = Stage
    context_object_name = "stages"


class SettingView(LoginRequiredMixin, TemplateView):
    template_name = "main/setting.html"


class StageViewSet(LoginRequiredMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Stage.objects.all().prefetch_related("questions", "completed_users")
    serializer_class = StageSerializer


class StageDetailView(LoginRequiredMixin, DetailView):
    model = Stage
    template_name = "main/stage_detail.html"

    def get_queryset(self):
        return Stage.objects.prefetch_related("questions", "completed_users")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stage = context["stage"]

        first_question = stage.questions.filter(question_number=1).first()
        context["first_question"] = first_question

        completed_count = stage.questions.filter(
            completed_users=self.request.user
        ).count()
        context["completed_count"] = completed_count

        return context


class QustionDetailView(LoginRequiredMixin, DetailView):
    model = Question
    template_name = "main/question_detail.html"

    def get_queryset(self):
        return Question.objects.prefetch_related("stage", "completed_users")


def social_account_confirmation(request):
    email = request.session.get("social_email")
    provider = request.session.get("social_account_provider")
    uid = request.session.get("social_account_uid")

    if request.method == "POST":
        password = request.POST.get("password")

        if email and password:
            try:
                user = CustomUser.objects.get(email=email)
                user = authenticate(request, email=email, password=password)

                if user:
                    login(request, user)
                    SocialAccount.objects.get_or_create(
                        user=user, provider=provider, uid=uid
                    )
                    del request.session["social_email"]
                    del request.session["social_account_provider"]
                    del request.session["social_account_uid"]

                    return redirect("index")
                else:
                    return render(
                        request,
                        "account/social_account_confirmation.html",
                        {"email": email, "error": "パスワードが間違っています。"},
                    )

            except CustomUser.DoesNotExist:
                pass

    return redirect("account_login")
