from django.db import models
from django.contrib.auth.models import User
from patient import settings
from phone_field import PhoneField
# from ckeditor.fields import RichTextField
# Create your models here.

class Department(models.Model):
    departmentname=models.TextField(max_length=50)

    def __str__(self):
        return self.departmentname


class DoctorProfile(models.Model):
    fullname=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    contact=PhoneField(max_length=50)
    specialization=models.ForeignKey(Department)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,default=1)

    def __str__(self):
        return self.fullname
