from django.contrib import admin

from .models import PatientProfile,Medicine
# Register your models here.
admin.site.register(PatientProfile)
admin.site.register(Medicine)
