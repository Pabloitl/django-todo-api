from factory.django import DjangoModelFactory
from factory import Faker

from tasks.models import Task

from datetime import date


class TaskFactory(DjangoModelFactory):
    class Meta:
        model = Task

    title = Faker("job")
    due = Faker("date", end_datetime=date.today())
    description = Faker("text")
