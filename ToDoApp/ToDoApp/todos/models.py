from django.db import models

from ToDoApp.todos.choices import StateChoice


class Category(models.Model):
    name = models.CharField(
        max_length=15,
    )


class Todos(models.Model):
    title = models.CharField(
        max_length=30,
    )

    description = models.TextField()

    state = models.BooleanField(
        choices=[
            (True, StateChoice.DONE),
            (False, StateChoice.NOT_DONE),
        ],
        default=False,
    )

    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
