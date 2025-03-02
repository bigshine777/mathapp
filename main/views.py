from django.views.generic import TemplateView
from allauth.account.views import SignupView
from .forms import CustomSignupForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from allauth.socialaccount.models import SocialAccount
from .models import CustomUser


class IndexView(TemplateView):
    template_name = "main/index.html"


class SettingView(TemplateView):
    template_name = "main/setting.html"


class CustomSignupView(SignupView):
    form_class = CustomSignupForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs


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
