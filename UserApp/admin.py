from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model=Profile
    fields=["user", "role"]
    search_fields = ['user',"role"]
    