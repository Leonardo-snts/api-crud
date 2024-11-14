from django.db import models
from django.core.exceptions import ValidationError

class Task(models.Model):
    tarefa = models.CharField(max_length=255, unique=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_final = models.DateField()
    ordem = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.tarefa

