from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^details/(?P<id>\d+)/$', views.details, name='details')
]
