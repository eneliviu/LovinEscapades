from django.contrib import admin
from .models import (Trip, Note, Image, Comment, Activity)

# Register your models here.

admin.site.register(Trip)
admin.site.register(Note)
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Activity)
