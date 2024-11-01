from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    language = models.CharField(
        max_length=30,
        choices=[
            ('es', 'Español'),
            ('en', 'English'),
        ],
        default='es'
        )
    
    def __str__(self):
        return self.user.username
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        else:
            instance.profile.save()

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()