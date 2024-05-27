from django import forms
from .models import *

class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post','name','email','subject','message']