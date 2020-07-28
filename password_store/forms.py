from django import forms
from .models import User
import hashlib
from passlib.hash import argon2 as a2


class UserForm(forms.ModelForm):
    def clean_password(self):
        password = self.cleaned_data["password"]
        password = a2.using(rounds=30).hash(password)
        return password

    class Meta:
        model = User
        fields = ["username", "password"]
