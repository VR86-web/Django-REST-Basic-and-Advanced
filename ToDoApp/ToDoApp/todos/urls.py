from django.urls import path

from ToDoApp.todos import views

urlpatterns = [
    path('', views.TodoListApiView.as_view(), name='todo-list-create'),

]