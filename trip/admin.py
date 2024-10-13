from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import (Trip, Image, Profile)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        return super(UserAdmin, self).get_inline_instances(request, obj)


# Unregister User
admin.site.unregister(User)

# Unregister Groups
admin.site.unregister(Group)

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Trip)
admin.site.register(Image)
admin.site.register(Profile)
