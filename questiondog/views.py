from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth.models import User
from .models import DogPost, Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST

# Create your views here.


def homepage(request):
    if request.user.is_authenticated:
        dogposts = DogPost.objects.order_by('-created_at')
        return render(request, 'core/home.html', {'dogposts': dogposts})
    else:
        return redirect('accounts/login/')


@login_required
def profile(request):
    posts = DogPost.objects.filter(user = request.user)
    comments = Comment.objects.filter(commentUser = request.user)
    return render(request, 'core/profile.html', {'posts': posts, 'comments': comments, } )

@login_required
def postdetail(request, pk):
    dogpost = DogPost.objects.get(pk=pk)
    coments = Comment.objects.filter(dogpost_id=pk).order_by('-created_at')
    return render(request, 'core/dogpostdetail.html', {'dogpost': dogpost, 'comments': coments, })

@login_required
def createPost(request):
    pass

@login_required
def createComment(request):
    pass

