# imageapi/urls.py

from django.urls import path
from .views import CaptchaImageView
from . import views

urlpatterns = [
    path('captcha/', CaptchaImageView.as_view(), name='captcha-image-upload'),
    path('captcha', CaptchaImageView.as_view(), name='captcha-image-upload'),
    path('captcha/<str:task_id>', views.get_captcha_task, name='get_captcha_task'),
]
# http://127.0.0.1:8000/api/captcha
#  http://127.0.0.1:8000/api/captcha/45639d4a-e4b9-4fbf-bbc1-51ee640ebd