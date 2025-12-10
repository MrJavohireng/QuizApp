from django.db import models
from django.contrib.auth.models import User
roles=[("Teacher","Teacher"),("Student","Student"), ("Admin","Admin")]
class Profile(models.Model):
    user=models.OneToOneField(to=User, on_delete=models.CASCADE)
    role=models.TextField(choices=roles)