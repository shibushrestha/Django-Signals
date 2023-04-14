from django.apps import AppConfig

from django.core.signals import request_finished
from django.db.models.signals import post_save

class DsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'DS'

    def ready(self):
        from django.contrib.auth.models import User
        from . import signals
        request_finished.connect(receiver=signals.my_first_callback)

        post_save.connect(receiver=signals.create_user_profile, sender=User)