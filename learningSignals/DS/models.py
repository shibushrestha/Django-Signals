from django.db import models
from django.contrib.auth.models import User


# A user profile will be created whenever a user gets register using  the post_save signal.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    mobile_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username
