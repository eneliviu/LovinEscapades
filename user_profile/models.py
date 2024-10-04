from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# from trip.models import Trip


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
    author_name = models.CharField(max_length=50, default="Anonymous")
    user_info = models.CharField(max_length=50, default="Enthusiast user")
    body = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.author_name}'s testimonial"


# class About(models.Model):
#     """
#     Stores a single about me text
#     """
#     title = models.CharField(max_length=200)
#     profile_image = CloudinaryField('image', default='placeholder')
#     updated_on = models.DateTimeField(auto_now=True)
#     content = models.TextField()

#     def __str__(self):
#         return self.title


# class CollaborateRequest(models.Model):
#     """
#     Stores a single collaboration request message
#     """
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#     message = models.TextField()
#     read = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Collaboration request from {self.name}"
