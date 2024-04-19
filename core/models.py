from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10)
    phone_no = models.BigIntegerField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['password','phone_no']

    def __str__(self):
        return self.email