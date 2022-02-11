from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Creates the initial users for the system.'

    def handle(self, *args, **options):
        get_user_model().objects.create_superuser('admin', 'admin@admin.com', 'admin')
