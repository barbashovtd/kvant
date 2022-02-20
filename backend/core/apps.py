from django.apps import AppConfig
from django.db.models.signals import pre_save


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"

    def ready(self) -> None:
        from .models import Student, Teacher
        from .signals import qr_create

        return super().ready()
