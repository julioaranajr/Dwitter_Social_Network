# dwitter/admin.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile)
        user_profile.save()

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
