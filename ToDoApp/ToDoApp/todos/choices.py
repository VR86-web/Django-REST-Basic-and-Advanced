from django.db import models


class StateChoice(models.TextChoices):
    DONE = 'DONE', 'DONE'
    NOT_DONE = 'NOT_DONE', 'NOT_DONE'
