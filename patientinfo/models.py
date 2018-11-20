from django.db import models
from phone_field import PhoneField
from comment.models import Comment
from doctorinfo.models import DoctorProfile
# Create your models here.

gender=(('m','Male'),('f','Female'))
class PatientProfile(models.Model):
    full_name=models.CharField(max_length=100)
    gender=models.CharField(max_length=10,choices=gender)
    age=models.CharField(max_length=10)
    address=models.CharField(max_length=50)
    contact=PhoneField(max_length=100)
    related_doc=models.ForeignKey(DoctorProfile,default=1)


    def __str__(self):
        return self.full_name


class Medicine(models.Model):
    medicine_name=models.CharField(max_length=100)
    start_date=models.DateField(max_length=50)
    dose=models.CharField(max_length=50)
    end_date=models.DateField(max_length=50)
    comment=models.ForeignKey(Comment, default=1)

    def __str__(self):
        return self.medicine_name
