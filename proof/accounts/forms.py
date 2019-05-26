from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo

class UserForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(label='First Name', required=True)
    last_name = forms.CharField(label='Last Name', required=True)
    email = forms.EmailField(max_length=200, required=True)

    class Meta():
        model = User
        fields = ('first_name','last_name','email', 'is_staff')
        exclude = ('password',)

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model= UserProfileInfo
        fields = ('picture',)
