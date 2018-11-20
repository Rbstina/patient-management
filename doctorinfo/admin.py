from django.contrib import admin

# Register your models here.
from .models import DoctorProfile,Department
admin.site.register(DoctorProfile)
admin.site.register(Department)
