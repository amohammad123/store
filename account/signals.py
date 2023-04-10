from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def createprofile(sender, instance, created=False, **kwargs):
    if created:
        Profile.objects.create(user_id=instance.id)

@receiver(post_delete, sender=settings.AUTH_USER_MODEL)
def delete_profile(sender, instance, deleted=False, **kwargs):
    if deleted:
        Profile.objects.delete(user_id=instance.id)
