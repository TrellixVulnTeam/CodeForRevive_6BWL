from django import forms
from .models import SignUp


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    confrom_pass = forms.CharField(widget=forms.PasswordInput(), required=True)

    class Meta:
        model = SignUp
        fields = '__all__'


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    class Meta:
        model = SignUp
        fields = ['email_id', 'password']
