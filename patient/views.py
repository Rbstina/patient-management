from django.http import HttpResponse
from django.shortcuts import render
from slider.models import Slider


def home(request):
    context={
    'slider': Slider.objects.all()[0],
    'slider2': Slider.objects.all()[1:],
    }
    return render(request,"index.html",context)
