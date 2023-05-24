from django.urls import path
from django.urls import re_path as url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.question, name='question'),
    path('<int:question_id>/essay<int:essay_id>/', views.essay, name='essay'),
]