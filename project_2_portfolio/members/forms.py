# forms.py
from django import forms

class YourForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    location = forms.CharField(max_length=100)
    contact = forms.CharField(max_length=15)
    language = forms.CharField(max_length=50)
    skill = forms.CharField(max_length=100)
    work_experience = forms.CharField(max_length=200)
    education = forms.CharField(max_length=200)
    project = forms.CharField(max_length=200)
    link = forms.URLField()
    summary = forms.CharField(widget=forms.Textarea)
