from django.db import models
from django.contrib.auth.models import User

class DogPost(model.Models):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=550)
    user = models.ForeignKey(to=User, related_name='logs', on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.title}'

class Comment(model.Models):
    commentBody= models.CharField(max_length=250)
    commentUser = models.ForeignKey(to=User, related_name='logs', on_delete=models.CASCADE )
    dogpost = models.ForeignKey(to=DogPost, related_name='dog-posts', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.dogpost}: {self.commentBody}'

# class VoteLog(model.Models):
    
