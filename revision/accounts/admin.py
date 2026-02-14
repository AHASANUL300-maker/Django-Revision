from django.contrib import admin
from accounts.models import AwesomeCustomUser, Student, ImageModel
# Register your models here.

admin.site.register(AwesomeCustomUser)
admin.site.register(Student)
admin.site.register(ImageModel)