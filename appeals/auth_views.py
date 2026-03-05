from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

def login_view(request):
    if request.user.is_authenticated:
        return redirect("/appeals/adminpanel/")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("/appeals/adminpanel/")
    else:
        form = AuthenticationForm()

    return render(request, "auth/login.html", {"form": form})

def register_view(request):
    if request.user.is_authenticated:
        return redirect("/appeals/adminpanel/")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/appeals/adminpanel/")
    else:
        form = UserCreationForm()

    return render(request, "auth/register.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("/auth/login/")