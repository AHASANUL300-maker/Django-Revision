from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.managers import AwesomeUserManager
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from PIL import Image
import os
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

# Using the signals
# Model on which the signal is applied
class Student(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=(("Male", "Male"), ("Female", "Female")))
    age = models.IntegerField(null=True, blank=True)
    student_id = models.CharField(max_length=10, null=True, blank=True)

# Signal Code
@receiver(post_save, sender=Student)
def save_student(sender, instance, created, **kwargs):
    print(sender, instance)
    print(created) # A Boolean value
    if created:
        instance.student_id = f"STU-000{instance.id}"
        instance.save()

        print("Student object created")

# Using Signals to create Thumbnails

class ImageModel(models.Model):
    original_image = models.ImageField(upload_to="images/")
    thumbnail_mini = models.ImageField(upload_to="images/thumbnails", null=True, blank=True)
    thumbnail_small = models.ImageField(upload_to="images/thumbnails", null=True, blank=True)
    thumbnail_medium = models.ImageField(upload_to="images/thumbnails", null=True, blank=True)
    thumbnail_large = models.ImageField(upload_to="images/thumbnails", null=True, blank=True)


#The Signal code -> Automatic creates the 3 size thumbnails when user uploads an image
@receiver(post_save, sender=ImageModel)
def create_thumbnail(sender, instance, created, **kwargs):
    if created:
        sizes = {
            "thumbnail_mini": (50, 50),
            "thumbnail_small": (150, 150),
            "thumbnail_medium": (400, 400),
            "thumbnail_large": (800, 800)
        }

        for fields, size in sizes.items():
            img = Image.open(instance.original_image.path)
            img.thumbnail(size, Image.Resampling.LANCZOS)
            thumb_name, thumb_extension = os.path.split(instance.original_image.name)
            thumb_extension = thumb_extension.lower()
            thumb_filename = f"{thumb_name}_{size[0]}X{size[1]}{thumb_extension}"
            thumb_path = f"thumbnails/{thumb_filename}"
            img.save(thumb_path)
            setattr(instance, fields, thumb_path)

