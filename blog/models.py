from django.db import models
from django import forms
from django.contrib.auth.models import User

class Entry(models.Model):
    author = models.ForeignKey(User, blank=True)
    title = models.CharField(max_length=50)
    post = models.TextField(max_length=2000)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.title
    
class Comment(models.Model):
    author = models.ForeignKey(User, blank=True)
    entry = models.ForeignKey(Entry)
    text = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.text
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput)
    
class SignupForm(forms.Form):
    username = forms.CharField(max_length=25)
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    