"""
mathapp プロジェクトの Django 設定ファイル。

'django-admin startproject' により生成されました (Django 5.1.3 使用)。

このファイルの詳細については以下を参照してください:
https://docs.djangoproject.com/ja/5.1/topics/settings/

すべての設定項目とその値の一覧については以下を参照してください:
https://docs.djangoproject.com/ja/5.1/ref/settings/
"""

import os
from dotenv import load_dotenv

# .env の読み込み
load_dotenv()

from pathlib import Path

# プロジェクト内のパスを簡単に指定できるように、BASE_DIR を定義
BASE_DIR = Path(__file__).resolve().parent.parent

LANGUAGE_CODE = "ja"
TIME_ZONE = "Asia/Tokyo"

# 開発用のクイックスタート設定 - 本番環境では不適切
# 本番環境用の設定チェックリスト:
# https://docs.djangoproject.com/ja/5.1/howto/deployment/checklist/

# 【重要】本番環境では SECRET_KEY を安全に管理すること
SECRET_KEY = "django-insecure-!9x3dkv!0gvbnkyp8sfwdi5v5c4uywdjsjq0%js4d1nw#ae$=!"

# 【重要】本番環境では DEBUG を False にすること
DEBUG = True

# 許可するホストのリスト (本番環境では適切に設定すること)
ALLOWED_HOSTS = []


# アプリケーションの定義

INSTALLED_APPS = [
    "django.contrib.admin",  # 管理サイト
    "django.contrib.auth",  # 認証システム
    "django.contrib.contenttypes",  # コンテンツタイプ (汎用的なモデル管理)
    "django.contrib.sessions",  # セッション管理
    "django.contrib.messages",  # メッセージフレームワーク
    "django.contrib.staticfiles",  # 静的ファイル管理
    "main",  # mainアプリケーションのインストール
    "allauth",  # allauthの追加
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
]

SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",  # セキュリティ強化のためのミドルウェア
    "django.contrib.sessions.middleware.SessionMiddleware",  # セッション管理用のミドルウェア
    "django.middleware.common.CommonMiddleware",  # 一般的なリクエスト処理
    "django.middleware.csrf.CsrfViewMiddleware",  # CSRF対策
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # 認証処理
    "django.contrib.messages.middleware.MessageMiddleware",  # メッセージフレームワーク
    "django.middleware.clickjacking.XFrameOptionsMiddleware",  # クリックジャッキング対策
    "allauth.account.middleware.AccountMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]

# プロジェクトのルート URL 設定ファイル
ROOT_URLCONF = "mathapp.urls"

# テンプレートエンジンの設定
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",  # Django のテンプレートエンジンを使用
        "DIRS": [],  # テンプレートディレクトリを指定する場合はここに追加
        "APP_DIRS": True,  # 各アプリ内の `templates/` ディレクトリを自動で認識
        "OPTIONS": {
            "context_processors": [  # テンプレートで利用可能なコンテキストプロセッサ
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI アプリケーションの設定 (本番環境で使用)
WSGI_APPLICATION = "mathapp.wsgi.application"


# データベースの設定
# https://docs.djangoproject.com/ja/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # SQLite を使用
        "NAME": BASE_DIR / "db.sqlite3",  # データベースファイルのパス
    }
}

STATICFILES_DIRS = [BASE_DIR / "static"]

AUTH_USER_MODEL = "main.CustomUser"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",  # Djangoの通常認証
    "allauth.account.auth_backends.AuthenticationBackend",  # allauth認証
]

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": os.getenv("GOOGLE_CLIENT_ID"),
            "secret": os.getenv("GOOGLE_CLIENT_SECRET"),
            "key": "",
        },
        "SCOPE": ["profile", "email"],
        "AUTH_PARAMS": {"access_type": "online"},
    }
}

SOCIALACCOUNT_ADAPTER = "main.adapters.SocialAccountAdapter"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

LOGIN_REDIRECT_URL = "/"  # ログイン後のリダイレクト先
ACCOUNT_LOGIN_METHODS = {"username", "email"}
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True

ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGOUT_REDIRECT_URL = "/accounts/login"  # ログアウト後のリダイレクト先

import os

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# パスワードバリデーション
# https://docs.djangoproject.com/ja/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # 最低文字数のチェック
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # よくあるパスワードを防ぐ
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # 数字のみのパスワードを防ぐ
    },
]


# 言語とタイムゾーンの設定
# https://docs.djangoproject.com/ja/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"  # 言語設定 (日本語なら "ja" に変更)

TIME_ZONE = "UTC"  # タイムゾーン (日本時間なら "Asia/Tokyo" に変更)

USE_I18N = True  # 国際化対応を有効化

USE_TZ = True  # タイムゾーンを有効化


# 静的ファイル (CSS, JavaScript, 画像など) の設定
# https://docs.djangoproject.com/ja/5.1/howto/static-files/

STATIC_URL = "static/"  # 静的ファイルのURLパス

# デフォルトのプライマリーキーのフィールドタイプ
# https://docs.djangoproject.com/ja/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = (
    "django.db.models.BigAutoField"  # モデルの ID フィールドに BigAutoField を使用
)
