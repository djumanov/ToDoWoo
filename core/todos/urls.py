from django.urls import path

from .views import TodoCreateView


urlpatterns = [
    path('', TodoCreateView.as_view(), name='todo_create'),
]
