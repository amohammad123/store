from django import forms
from account.models import *
from django.contrib.auth.forms import UserChangeForm


class ProfileRegister(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)

    class Meta:
        model = Profile
        fields = ['profile_image', 'gender', 'born_date', 'credit']

class ProfileEdit(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image', 'gender', 'born_date', 'credit']

class UserEdit(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields=["first_name","last_name","email"]
    password=None