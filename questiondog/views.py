from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth.models import User
from .models import DogPost, Comment, CommentVoteLog
from .forms import QuestionForm, CommentForm, CommentVoteLogForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from django.utils import timezone

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
    if request.method == "POST" and "subcomment":
        form = CommentForm(request.POST)
        commentBody = request.POST.get('body')
        if form.is_valid():
            post = form.save(commit=False)
            post.commentUser = request.user
            post.created_at = timezone.now()
            post.dogpost = dogpost
            post.save()
            return redirect(f'/goodboi/{pk}/')

    else:    
        form = CommentForm()
    return render(request, 'core/dogpostdetail.html', {'dogpost': dogpost, 'comments': coments, 'form': form, })

@login_required
def vote(request, pk):
    if request.method == "POST" and "upvote":
        form = CommentVoteLogForm(request.POST)
        # log = get or create (commentvotelog), returns bolean 
        comment = get_object_or_404(Comment, pk=pk)
        if form.is_valid():
            log = form.save(commit=False)
            log.voter = request.user
            log.comment = comment
            log.rankValue = 1
            log.save()
            return redirect(f'/goodboi/{comment.dogpost.pk}/')
    elif request.method == "POST" and "downvote":
        return redirect(f'/goodboi/{comment.dogpost.pk}/')

@login_required
def create_post(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        title = request.POST.get('title')
        body = request.POST.get('body')
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.created_at = timezone.now()
            post.save()
            return redirect('profile')
    else:    
        form = QuestionForm()
    return render(request, 'core/newbork.html', {'form': form})

@login_required
def createComment(request):

    pass

