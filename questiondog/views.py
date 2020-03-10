from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth.models import User
from .models import DogPost, Comment

# Create your views here.


def homepage(request):
    return render(request, 'core/home.html',)