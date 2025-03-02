from django.core.exceptions import ValidationError
from allauth.account.forms import SignupForm
from allauth.account.models import EmailAddress
from allauth.account.utils import send_email_confirmation
from .models import CustomUser


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)  # request を取り除いて保存
        super().__init__(*args, **kwargs)  # Django の Form に不要な kwargs を渡さないようにする

    def clean_email(self):
        email = self.cleaned_data["email"]
        user = CustomUser.objects.filter(email=email).first()

        if user:
            email_address = EmailAddress.objects.filter(email=email).first()
            if email_address:
                if email_address.verified:
                    raise ValidationError("このメールアドレスはすでに登録されています。")
                else:
                    send_email_confirmation(self.request, user)
                    raise ValidationError("このメールアドレスは未認証のため、確認メールを再送信しました")

        return email
