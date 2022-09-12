from django.contrib import admin
from django.urls import include, re_path
from django.urls import path

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^Vote/', include('Vote.urls')),
    path('', include('Vote.urls')),
    re_path(r'^records/', include('records.urls')),
]
