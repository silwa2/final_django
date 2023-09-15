
from django.core.management.base import BaseCommand

from magazin_app.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(name='John', email='john@example.com', phone='89076543234', address='Rossia',
                    registered_at='01.01.1999')
        user.save()
        self.stdout.write(f'{user}')
