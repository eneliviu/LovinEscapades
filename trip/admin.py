from django.contrib import admin
from django.contrib.auth.models import (Group, User)
from .models import (Trip, Note, Image, Comment, Activity, UserProfile)


# Unregister Groups
admin.site.unregister(Group)

# Register your models here.
admin.site.register(Trip)
admin.site.register(Note)
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Activity)
admin.site.register(UserProfile)
