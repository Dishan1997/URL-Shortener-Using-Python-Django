from contextlib import redirect_stderr
#from typing import _get_type_hints_obj_allowed_types
from winreg import REG_RESOURCE_REQUIREMENTS_LIST
from wsgiref.util import request_uri
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages, auth

# Create your views here.
def login(request):
    if not request.user.is_authenticated:
     if request.method == "POST":
         if request.POST['email'] and request.POST['password']:
             try:
                 user = User.objects.get(email = request.POST['email'])
                 auth.login(request, user)
                 if request.POST['next'] !='':
                     return redirect(request.POST.get('next'))
                 else:
                     return redirect('/')
                 return redirect('/')
             except User.DoesNotExist:
                 return render(request, 'login.html', {'error': "User Doesn't Exist"})
         else:
             return render(request, 'login.html', {'error': "Empty Fields"})
            
     else:
         return render(request, 'login.html')
    else:
        return redirect('/')  
     


def signup(request):
    if request.method =="POST":
        ##do something
        if request.POST['password']== request.POST['password2']:
            if request.POST['username'] and request.POST['email'] and request.POST['password']:
               try:
                user = User.objects.get(email = request.POST['email'])
                return render(request, 'signup.html', {'error': "User Already Exist"})
               except User.DoesNotExist:
                User.objects.create_user(
                    username = request.POST['username'],
                    email= request.POST['email'],
                    password=request.POST['password'],
                )
                messages.success(request, "Signup Successful <br/> Login Here")
                return redirect(login)
                pass
            else:
                return render(request, 'signup.html', {'error': "Empty Fields"})
        else:
            return render(request, 'signup.html', {'error': "Password Don't Match"})
    else:
        return render(request, 'signup.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/login')