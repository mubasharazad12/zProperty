from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Question, PropertyInquiry
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


class QuestionForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg form-control-a",
        "placeholder": "Full Name"
    }))

    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg form-control-a",
        "placeholder": "Email"
    }))
    phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg form-control-a",
        "placeholder": "Phone#"
    }))

    Subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg form-control-a",
        "placeholder": "Subject"
    }))
    Question = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Message"
    }))

    class Meta:
        model = Question
        fields = ["name", "email", "phone", "Subject", "Question"]


class PropertyInquiryForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg form-control-a",
        "placeholder": "Full Name"
    }))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg form-control-a",
        "placeholder": "Email"
    }))
    phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg form-control-a",
        "placeholder": "Phone#"
    }))
    Subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg form-control-a",
        "placeholder": "Subject"
    }))
    Question = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Message"
    }))

    class Meta:
        model = PropertyInquiry
        fields = ["name", "email", "phone", "Subject", "Question"]
