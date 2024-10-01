from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    follows = models.ManyToManyField('self',
                                     related_name='followed_by',
                                     symmetrical=False,
                                     blank=True)
    date_modified = models.DateTimeField(User, auto_now=True)

    def __str__(self):
        return self.user.username


class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Testimonial"

