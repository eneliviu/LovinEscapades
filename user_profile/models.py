from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


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
    '''
    Stores a single testimonial text
    '''
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='testimonials')
    author_name = models.CharField(
        max_length=50,
        blank=False,
        default="Anonymous",
        validators=[MinLengthValidator(2)]
        )
    user_info = models.CharField(
        max_length=50,
        blank=False,
        default="Enthusiast user",
        validators=[MinLengthValidator(2)]
        )
    body = models.TextField(
        blank=False,
        validators=[MinLengthValidator(20)]
        )
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.author_name}'s testimonial"
