from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    due = models.DateField()
    description = models.TextField()
