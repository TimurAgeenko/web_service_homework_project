from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Loads fixtures into database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--email',
            '-e',
            type=str,
            help='User`s email which will own products',
            default='admin@mail.com'
        )

    def handle(self, *args, **kwargs):
        User = get_user_model()
        email = kwargs['email']

        try:
            target_user = User.objects.get(email=email)
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR('User not found'))
            return

        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command('loaddata', 'categories_fixture')
        call_command('loaddata', 'products_fixture')

        unowned_products = Product.objects.filter(owner__isnull=True)

        unowned_products.update(owner=target_user)

        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixtures.'))
