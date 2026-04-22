from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Creates managers group if it isn`t exists, adds permissions to it and adds current user into group'

    def add_arguments(self, parser):
        parser.add_argument(
            '--group',
            '-g',
            type=str,
            help='Group name',
            default='Контент менеджер'
        )
        parser.add_argument(
            '--email',
            '-e',
            type=str,
            help='User`s email which will be added to managers group'
        )

    def handle(self, *args, **kwargs):
        User = get_user_model()
        email = kwargs['email']
        group, _ = Group.objects.get_or_create(name=kwargs['group'])

        perms = Permission.objects.filter(
            content_type__app_label='blog',
            codename__in=['can_unpublish_post', 'delete_blogpost']
        )

        group.permissions.set(perms)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR('User with current email not found'))
            return

        user.groups.add(group)

        self.stdout.write(self.style.SUCCESS('Successfully added user to managers group.'))