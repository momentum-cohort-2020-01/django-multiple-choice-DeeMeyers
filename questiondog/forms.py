from django import forms
from .models import DogPost, Comments

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comments
        fields = ('commentBody', )
