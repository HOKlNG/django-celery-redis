from django import forms
from app_accounts.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'nickname', 'password']