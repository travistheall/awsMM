from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Photo


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Photo)
def create_photo(sender, instance, created, **kwargs):
    if created:
        print(instance)
        # Photo.objects.get(user=instance)
