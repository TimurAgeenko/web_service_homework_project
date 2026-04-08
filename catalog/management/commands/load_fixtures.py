from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Loads fixtures into database'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command('loaddata', 'categories_fixture')
        call_command('loaddata', 'products_fixture')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixtures.'))
