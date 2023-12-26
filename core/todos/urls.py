from django.urls import path

from .views import TodoCreateView, TodoDetailView, CompletedTodosView


urlpatterns = [
    path('', TodoCreateView.as_view(), name='todo_create'),
    path('<int:pk>/', TodoDetailView.as_view(), name='todo_detail'),
    path('completed/', CompletedTodosView.as_view(), name='completed_todos'),
]
