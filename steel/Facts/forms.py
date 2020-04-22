from django import forms
from .models import UserProfile,Link

class UserForm(forms.ModelForm):
    class Meta:
        model= UserProfile
        exclude=('user',)

class LinkForm(forms.ModelForm):
    class Meta:
        model=Link
        fields=('title','description')
