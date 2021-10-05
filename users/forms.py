from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User  # save it to the User model
        fields = ['username', 'email', 'password1', 'password2']  # Fields in form, in this order
