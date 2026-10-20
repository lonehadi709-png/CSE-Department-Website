
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django import forms

from .models import Faculty, Notice, Event


User = get_user_model()


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        labels = {
            "username": "Username",
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email Address",
        }


def home(request):
    context = {
        "faculty_members": Faculty.objects.all(),
        "notices": Notice.objects.all(),
        "events": Event.objects.all(),
    }
    return render(request, "core/home.html", context)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = UserCreationForm()

    return render(request, "core/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("dashboard")
    else:
        form = AuthenticationForm()

    return render(request, "core/login.html", {"form": form})


@login_required
def dashboard(request):
    context = {
        "notices": Notice.objects.all(),
        "events": Event.objects.all(),
    }
    return render(request, "core/dashboard.html", context)


@login_required
def student_profile(request):
    return render(request, "core/profile.html", {"user": request.user})


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = StudentProfileForm(
            request.POST,
            instance=request.user
        )
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = StudentProfileForm(instance=request.user)

    return render(
        request,
        "core/edit_profile.html",
        {"form": form}
    )


def user_logout(request):
    logout(request)
    return redirect("home")
