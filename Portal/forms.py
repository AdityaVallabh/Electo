from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Voter

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Voter
        fields = ('username', 'name', 'class_sec', 'house', 'stage', 'password')
        
class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = Voter
        fields = ('username', 'name', 'class_sec', 'house', 'stage')
        