from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('ulib.urls')),
    path('admin/', admin.site.urls),
]
