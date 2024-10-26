from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@mail.ru',
            first_name='admin',
            login='mail',
            password='Blev2011',
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )
        user.set_password('Blev2011')
        user.save()