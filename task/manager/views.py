from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from . import forms


def LoginPage(request):
    obj = forms.LoginForm()
    return render(request, 'base.html', {'obj': obj})


def signUpPage(request):
    form = forms.SignUpForm()
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            email_id = form.cleaned_data['email_id']
            mobile_no = form.cleaned_data['mobile_no']
            password = form.cleaned_data['password']
            confrom_pass = form.cleaned_data['confrom_pass']
            form.save()
            return redirect("<h2>Hey congo you created your account</h2>")
    else:
        form = forms.SignUpForm()
        return render(request, 'signup.html', {'form': form})

