from rest_framework import serializers

from ToDoApp.todos.models import Category, Todos


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name',]
        read_only_fields = ['id',]


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = '__all__'
        read_only_fields = ['id',]