from django.contrib import admin
from django.urls import path, include
import todo.views

urlpatterns = [
    path('', todo.views.index),
    path('tasks/', include('todo.urls')),
]
