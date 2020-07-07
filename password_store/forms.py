from django import forms
from .models import User
import hashlib

class UserForm(forms.ModelForm):
    def clean_password(self):
        password = self.cleaned_data["password"]
        password = hashlib.sha512(bytes(password, "utf-8")).hexdigest()
        return password

    class Meta:
        model = User
        fields = ["username", "password"]
