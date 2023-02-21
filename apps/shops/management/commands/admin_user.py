from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = "Create superuser with username: 'admin', password: '1'"

    def handle(self, *args, **options):
        user = User.objects.create_user('admin', password='1', is_superuser=1, is_staff=1)
        print(f'\033[43m<SuperUser {user}: password=1>\033[92m  Created!\033[00m')
