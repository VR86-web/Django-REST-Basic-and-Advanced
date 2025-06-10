from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from ToDoApp.todos.models import Todos
from ToDoApp.todos.serializers import TodoSerializer


class TodoListApiView(ListCreateAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        queryset = Todos.objects.all()

        category = self.request.query_params.get('category')
        is_done = self.request.query_params.get('is_done')

        if category:
            queryset = queryset.filter(category__name=category)
        if is_done:
            queryset = queryset.filter(state=is_done.lower() == 'true')

        return queryset