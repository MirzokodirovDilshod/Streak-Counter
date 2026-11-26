from django import forms
from django.contrib.auth.models import User
from .models import Counter

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class CounterForm(forms.ModelForm):
    class Meta:
        model = Counter
        fields = ['title']