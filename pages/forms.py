from django import forms
from .models import *


class Nameform(forms.Form):
    name=forms.CharField(max_length=255)
    email=forms.EmailField()
    subject=forms.CharField(max_length=255)
    message=forms.CharField(widget=forms.Textarea)

class ContactForms(forms.ModelForm):
<<<<<<< HEAD

=======
>>>>>>> parent of 2a2282e (add captcha)
    class Meta:
        model = Contact
        fields = '__all__'


class Newsletterform(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'