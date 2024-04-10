from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('imageapi.urls')),
    path('api/', include('customerApp.urls')),
    path('', include('myapp.urls')),
]
#  https://primarydomain.com/api/createTask
#  https://primarydomain.com/api/getBalance