from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Autome creating superuser'

    def handle(self, *args, **options):
        user = get_user_model()
        user.objects.create_superuser(username='admin', password='admin', email='admin@aadmin.aadmin', is_superuser=True, is_staff=True)
        self.stdout.write(self.style.SUCCESS(f'Successfully create superuser'))
