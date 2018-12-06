from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from myaccount.models import UserProfile
from django.contrib.auth import authenticate
from .forms import RegisterForm,LoginForm
# Create your views here.


def register(request):
    if request.method=='GET':
        context={
        'form':RegisterForm(),
        }
        return render(request,'register.html', context)

    else:
        form=RegisterForm(request.POST)
        if form.is_valid():
            try:
                password=request.POST.get('password')
                re_password=request.POST.get('re_password')
                if password==re_password:
                    form.save()
                    return redirect('login')

                else:
                    return render(request,'register.html',{'form':form,'errmsg':'Password didnt match'})


            except:
                return render(request,'register.html',{'form':form})


        else:
            context={
            'form' :form,
            }
            return render (request,'register.html', context)

def login(request):
    if request.method=='GET':
        context={
        'form' :LoginForm(),
        }
        return render(request,'login.html',context)

    else:
        form=LoginForm(request.POST)
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            all_user=UserProfile.objects.all()
            if all_user.username==username:
                if all_user.password==password:
                    return render(request,'doctordashboard.html')
                else:
                    return render(request,'login.html',{'form':form,'errmsg':'Password didnt match'})

            else:
                return render(request,'login.html',{'form':form,'errmsg':'Username didnt match'})

        except:
            return render(request,'login.html',{'form':form})
