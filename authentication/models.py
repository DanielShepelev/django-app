from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import UniqueConstraint

class FoodiUser(AbstractUser):
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=1000)
    email = models.CharField(max_length=80)
    prefrence = models.JSONField()

    USERNAME_FIELD = "username"

    class Meta:
        constraints = [UniqueConstraint(fields=["username"], name="user_username_unq")]

    def __str__(self):
        return self.item_type
