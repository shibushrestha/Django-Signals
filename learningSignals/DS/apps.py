from django.apps import AppConfig
from django.core.signals import request_finished
from django.db.models.signals import post_save

class DsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'DS'

    def ready(self):
        from . import signals
        from django.contrib.auth.models import User

        request_finished.connect(signals.mySignal)
        post_save.connect(receiver=signals.create_user_profile, sender=User)
