from dataclasses import fields
from .models import Diary
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField


User = get_user_model()


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}


class DiaryCreateForm(ModelForm):
    class Meta:
        model = Diary
        fields = (
            'title',
            'content'
        )
