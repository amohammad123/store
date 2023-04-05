from django.apps import AppConfig


class AcountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ACOUNT'

    def ready(self):
        import ACOUNT.signals