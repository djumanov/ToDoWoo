from django.urls import path

from .views import TodoCreateView, TodoDetailView


urlpatterns = [
    path('', TodoCreateView.as_view(), name='todo_create'),
    path('<int:pk>/', TodoDetailView.as_view(), name='todo_detail'),
]
