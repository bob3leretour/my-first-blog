from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Post


class LoginForm(AuthenticationForm):

    class Meta:
        fields = ('username', 'password',)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

