# imageapi/urls.py

from django.urls import path
from .views import CaptchaImageView

urlpatterns = [
    path('captchaImgUpload/', CaptchaImageView.as_view(), name='captcha-image-upload'),
    path('captchaImgUpload', CaptchaImageView.as_view(), name='captcha-image-upload'),
]
#http://127.0.0.1:8000/api/captchaImgUpload