from django.db import models

# Create your models here.

#class Child(Parent): Single Inheritance

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    pass

class CaptchaTask(models.Model):
    task_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20)
    result = models.TextField(blank=True, null=True)



