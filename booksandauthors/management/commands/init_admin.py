from typing import Any

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args: tuple[Any, ...], **options: dict[str, Any]) -> None:
        if User.objects.count() == 0:
            username = "admin"
            password = "admin"
            print(f"Creating account for {username}")
            admin = User.objects.create_superuser(username=username, password=password)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print("Admin accounts can only be initialized if no Accounts exist")
