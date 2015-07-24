from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Post, Category
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginForm(AuthenticationForm):

    class Meta:
        fields = ('username', 'password')


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'photo','category')

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name',)




class ContactForm(forms.Form):
    sender = forms.EmailField(max_length=50)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget = forms.Textarea)
