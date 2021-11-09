from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Question
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["first_name", "last_name", "email", "phone", "Subject" ,"Question"]

