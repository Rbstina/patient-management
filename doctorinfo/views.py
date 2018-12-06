from django.shortcuts import render,redirect
from .models import DoctorProfile


# Create your views here.
def doctordashboard(request):
    context={
    'doctorinfo':DoctorProfile.objects.all(),
    }
    return render(request,'doctordashboard.html',context)
