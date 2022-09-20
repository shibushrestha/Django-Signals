def mySignal(sender, **kwargs):
    print("Request finished!")


from .models import UserProfile
# This is the receiver function which creates a user profile for each user when they get register in the app
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile.objects.create(user=instance)