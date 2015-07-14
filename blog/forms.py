from django import forms

from .models import Post


class LoginForm(forms.Form):

    class Meta:
        fields = ('username', 'password',)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

