from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import SocialAccount
from allauth.exceptions import ImmediateHttpResponse
from django.shortcuts import render
from .models import CustomUser


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        email = sociallogin.account.extra_data.get("email")

        if email:
            try:
                user = CustomUser.objects.get(email=email)

                if SocialAccount.objects.filter(
                    user=user, provider=sociallogin.account.provider
                ).exists():
                    sociallogin.connect(request, user)
                    return

                if not request.session.get("social_account_confirmed"):
                    request.session["social_email"] = email
                    request.session["social_account_provider"] = (
                        sociallogin.account.provider
                    )
                    request.session["social_account_uid"] = sociallogin.account.uid

                    response = render(
                        request,
                        "account/social_account_confirmation.html",
                        {"email": email},
                    )
                    raise ImmediateHttpResponse(response)

            except CustomUser.DoesNotExist:
                pass
