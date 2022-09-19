from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction

from tasks.factories import TaskFactory
from tasks.models import Task


class Command(BaseCommand):
    help = "Seed tasks"

    @transaction.atomic
    def handle(self, *args, **options):
        TASKS_COUNT = 15

        print("Removing all tasks ...")
        Task.objects.all().delete()

        print("seeding ...")
        [TaskFactory() for _ in range(TASKS_COUNT)]
