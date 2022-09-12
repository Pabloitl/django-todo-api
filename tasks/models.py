from django.db import models

from datetime import date


class Task(models.Model):
    title = models.CharField(max_length=100)
    due = models.DateField()
    description = models.TextField()

    @property
    def delayed(self) -> bool:
        print(self.due, type(self.due))
        return self.due < date.today()
