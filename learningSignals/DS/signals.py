from .models import UserProfile

def my_first_callback(sender, **kwargs):
    print("Request finished.")

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile.objects.create(user=instance)