from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Post
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)


class LoginForm(AuthenticationForm):

    class Meta:
        fields = ('username', 'password',)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

