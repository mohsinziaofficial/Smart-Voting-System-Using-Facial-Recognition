from django.urls import re_path
from django.urls import path
from . import views

app_name = 'Vote'
urlpatterns = [
    path("", views.index, name="index"),
    re_path(r'^login/', views.user_login, name='login'),
    re_path(r'^logout/', views.user_logout, name='logout'),
    re_path(r'^vote/', views.vote, name='vote'),
    re_path(r'^results/', views.results, name='results'),
    re_path(r'^home/', views.home, name='home'),
    re_path(r'^about/', views.about, name='about'),
    re_path(r'^voted/', views.voted, name='voted'),
    re_path(r'^details/', views.details, name='details'),
    re_path(r'^invalid/', views.invalid, name='invalid'),
    re_path(r'^casted/', views.casted, name='casted'),
    path(r'detect/', views.detect,name='detect'),
    re_path(r'^create_dataset$', views.create_dataset),
    re_path(r'^trainer$', views.trainer),
    re_path(r'^detect$', views.detect),
    re_path(r'^face_index$', views.face_index, name='face_index'),

]
