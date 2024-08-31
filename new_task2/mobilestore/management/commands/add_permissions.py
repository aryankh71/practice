from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Permission


class Command(BaseCommand):
    help = 'Assign specific permissions to existing users'

    def handle(self, *args, **kwargs):
        can_list = ['Can add mobile', 'Can change mobile', 'Can view mobile', 'Can delete mobile']
        permissions = []
        for can in can_list:
            try:
                permission = Permission.objects.get(name=can)
                permissions.append(permission)
            except Permission.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Permission with name "{can}" does not exist.'))

        users = User.objects.all()
        for user in users:
            for permission in permissions:
                if not user.has_perm(f'{permission.content_type.app_label}.{permission.codename}'):
                    user.user_permissions.add(permission)
                    self.stdout.write(
                        self.style.SUCCESS(f'Permission "{permission.name}" assigned to user: {user.username}'))
                else:
                    self.stdout.write(
                        self.style.WARNING(f'User {user.username} already has permission "{permission.name}".'))

        self.stdout.write(self.style.SUCCESS('Permissions assignment completed.'))