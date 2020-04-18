from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from TvShow.models import TvShow

def register(request): 
    form = RegisterForm(request.POST or None)
    if(form.is_valid()): #forms.py'deki clean metodunu çağırdık
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        email = form.cleaned_data.get("email")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username, first_name = first_name, last_name = last_name, email = email)
        newUser.set_password(password)
        newUser.save() #Kullanıcı Veri tabanına kaydedildi.
        login(request, newUser) #otomatik giriş yaptı
        messages.info(request,"Başarıyla Kayıt Oldunuz.")
        return redirect("index")
    context = {
        "form" : form
    }
    return render(request,"register.html", context)

def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    if(form.is_valid()):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        #Kullanıcı var mı sorgulamamız gerek. authenticate
        user = authenticate(username = username, password = password)
        if(user is None):
            messages.info(request,"Kullanıcı Adı veya Şifre Hatalı.")
            return render(request, "login.html", context)
        
        messages.info(request,"Hoş Geldiniz ")
        login(request,user)
        return redirect("index")

    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.info(request,"Hoşça kalın.")
    return redirect("index")

    