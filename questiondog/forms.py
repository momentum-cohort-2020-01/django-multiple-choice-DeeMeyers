from django import forms
from .models import DogPost, Comment

class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = DogPost
        fields = ('title', 'body' )


