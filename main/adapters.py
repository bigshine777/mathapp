from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        # 同じメールアドレスのアカウントをそのユーザーに紐づける

        email = sociallogin.account.extra_data.get("email")
        if email:
            try:
                user = User.objects.get(email=email)
                sociallogin.connect(request, user)
            except ObjectDoesNotExist:
                pass
