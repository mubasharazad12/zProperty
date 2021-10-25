from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
    return render(request, "Accounts/Login.html")


def logout_user(request):
    logout(request)
    return redirect('login')


def register_user(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "Accounts/Register.html", context)
