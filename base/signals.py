from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=HomeSetting)
def create_model(sender, instance, created=False, **kwargs):
    if created:
        Aboutus.objects.create(id=instance.id)
        Socialmedia.objects.create(id=instance.id)
        Images.objects.create(id=instance.id)
