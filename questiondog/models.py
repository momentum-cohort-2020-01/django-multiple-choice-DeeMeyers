from django.db import models
from users.models import User

class DogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=550)
    user = models.ForeignKey(to=User, related_name='logs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    commentBody= models.CharField(max_length=250)
    commentUser = models.ForeignKey(to=User, related_name='log', on_delete=models.CASCADE)
    dogpost = models.ForeignKey(to=DogPost, related_name='dogposts', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.dogpost}: {self.commentBody}'

class CommentVoteLog(models.Model):
    voter = models.ForeignKey(to=User, related_name='vote', on_delete=models.CASCADE)
    comment = models.ForeignKey(to=Comment, related_name='dogposts', on_delete=models.CASCADE, null=True, blank=True)
    rankValue = models.IntegerField()
    def __str__(self):
        return f'{self.comment}, {self.rankValue}'
