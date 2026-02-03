from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Store(models.Model):
    bmp_id = models.CharField(unique=True, max_length=100)
    strore_name = models.CharField(max_length=100)


    def __str__(self):
        return f"Store: {self.strore_name}, BMP: {self.bmp_id}"

