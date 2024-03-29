from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# A user profile will be created whenever a user gets register using  the post_save signal.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    mobile_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username

'''
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile.objects.create(user=instance)

post_save.connect(receiver=create_user_profile, sender=User)
'''