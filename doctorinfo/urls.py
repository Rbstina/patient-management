from django.conf.urls import url
from .import views

urlpatterns=[
    url(r'^doctordashboard/',views.doctordashboard,name='doctordashboard'),
]
