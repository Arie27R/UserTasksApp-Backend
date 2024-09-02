from django.db import models

# Create your models here.

class Tasks(models.Model):

    """
    Modelo que representa una tarea.

    Atributos:
        TASK_STATES (list): Lista de opciones permitidas para el campo State.
        TaskId (AutoField): Identificador único de la tarea.
        Title (CharField): Título de la tarea.
        Description (CharField): Descripción de la tarea.
        State (CharField): Estado actual de la tarea.
        ExpirationDate (DateField): Fecha de vencimiento de la tarea.
    """

    TASK_STATES = [
        ('pending', 'Pending'),
        ('in progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    TaskId = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=500)
    State = models.CharField(max_length=20, choices=TASK_STATES, default='pending')
    ExpirationDate = models.DateField()

    def __str__(self):
        return str(self.Title)
