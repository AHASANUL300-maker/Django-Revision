from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.managers import AwesomeUserManager
# Create your models here.


class AwesomeCustomUser(AbstractUser):

    username = None

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12, unique=True)
    profile_image = models.ImageField(upload_to="profile", null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AwesomeUserManager()


