from django.contrib import admin
from .models import DogPost, Comment, CommentVoteLog

admin.site.register(DogPost)
admin.site.register(Comment)
admin.site.register(CommentVoteLog)

# Register your models here.
