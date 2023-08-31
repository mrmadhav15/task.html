from django.urls import path
from . import views

urlpatterns = [
    path('url/task', views.task, name='task'),
]
