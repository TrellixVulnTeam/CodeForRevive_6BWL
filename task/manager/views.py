from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from . import forms
from django.http import HttpResponseRedirect, HttpResponse
from .models import SignUp


def LoginPage(request):
    if request.method == 'POST':
        obj = forms.LoginForm(request.POST)
        model = SignUp

        Email = ''
        Password = ''
        try:
            Email = obj.cleaned_data['email_id']
            Password = obj.cleaned_data['password']
        except:
            Email = 'dadhichhardik26@gmail.com'
            Password = 'yoyo'

        try:
            typed_email = model.objects.filter(email_id=Email).only("email").values_list()[0][2]
            typed_pass = model.objects.filter(password=Password).only("email").values_list()[0][4]
            typed_email = str(typed_email)
            typed_pass = str(typed_pass)
            print("----------", typed_email, typed_pass)
        except:
            pass

        if Email == typed_email and Password == typed_pass:
            print("entered in box")
            return HttpResponseRedirect('welcome/')
        else:
            return HttpResponse("<h2>User may not exist , please signUp first</h2>")
    else:
        obj = forms.LoginForm()
        return render(request, 'base.html', {'obj': obj})


def signUpPage(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email_id = form.cleaned_data['email_id']
            mobile_no = form.cleaned_data['mobile_no']
            password = form.cleaned_data['password']
            confrom_pass = form.cleaned_data['confrom_pass']
            form.save(commit=True)
            print(request)
            return HttpResponse("<h2>Hey congo you created your account</h2>")
    else:
        form = forms.SignUpForm()
        return render(request, 'signup.html', {'form': form})


def welcomePage(request):
    return render(request, 'afterLogin.html', None)
