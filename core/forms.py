from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Your Username',
            'class': 'w-full px-4 py-2 rounded-xl border'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Your Email',
            'class': 'w-full px-4 py-2 rounded-xl border'
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter Password',
            'class': 'w-full px-4 py-2 rounded-xl border'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password',
            'class': 'w-full px-4 py-2 rounded-xl border'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Your Username',
            'class': 'w-full px-4 py-2 rounded-xl border'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter Password',
            'class': 'w-full px-4 py-2 rounded-xl border'
        })
    )