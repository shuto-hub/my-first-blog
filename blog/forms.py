from django import forms

from .models import Post

from django.contrib.auth.models import User

from .models import Comment

from . import models

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class RegistrationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class CommentForm(forms.ModelForm):

    class Meta:
        model = models.Comment
        fields = ('text',)