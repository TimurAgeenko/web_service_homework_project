from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Loads fixtures into database'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command('loaddata', 'categories_fixture')
        call_command('loaddata', 'products_fixture')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixtures.'))
