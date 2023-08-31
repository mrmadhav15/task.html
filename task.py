from django.urls import path
from . import views

urlpatterns = [
    path('url/task', views.task, name='task'),
]

from django.shortcuts import render

def task(request):
    # Your dynamic data goes here
    context = {
        'data': 'Your dynamic data goes here'
    }
    return render(request, 'task.html', context)
