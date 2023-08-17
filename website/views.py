from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def home(request):
    # check to see if loging in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, f"Welcome {username}!") # how to remove this after a few seconds?
            # remove message after a second
            messages.success(request, f"Welcome {username}!")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("home")
    else:
        return render(request, "website/home.html", {})


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("home")


def register_user(request):
    return render(request, "register.html", {})
