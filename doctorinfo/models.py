from django.db import models
from patient import settings
from phone_field import PhoneField
# from ckeditor.fields import RichTextField
# Create your models here.

class Department(models.Model):
    departmentname=models.TextField(max_length=50)

    def __str__(self):
        return self.departmentname

gender=(('m','Male'),('f','Female'))
class DoctorProfile(models.Model):
    fullname=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    age=models.CharField(max_length=10,default=1)
    gender=models.CharField(max_length=10,choices=gender,default=1)
    contact=PhoneField(max_length=50)
    specialization=models.ForeignKey(Department)
    experience=models.CharField(max_length=100,default=1)
    image=models.ImageField(upload_to='media/',default=1)


    def __str__(self):
        return self.fullname
