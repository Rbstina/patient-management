from django.forms import ModelForm
from django import forms
from .models import UserProfile


class RegisterForm(ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    re_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=UserProfile
        fields=('full_name','email','username','phone_num','password','re_password','address','is_doctor','is_patient')



class LoginForm(ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=UserProfile
        fields=('username','password')
