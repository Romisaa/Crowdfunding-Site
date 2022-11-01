# This is for create a custom form with some extra fields other than that django provide
from cProfile import Profile
from dataclasses import field
import email
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile
from django.core.validators import RegexValidator
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField(validators=[RegexValidator('01[0125][0-9]{8}$')])

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone_number', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
        label="Username or Email*")

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())


# Creating new classes to upload profile picture

class UserUpdateForm(forms.ModelForm):
    # email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField(validators=[RegexValidator('01[0125][0-9]{8}$')])

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone_number']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
