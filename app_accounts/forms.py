from django import forms
from app_accounts.models import User

class UserForm(forms.ModelForm):
    password_confirm = forms.CharField(max_length=64, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email', 'nickname', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise forms.ValidationError("패스워드가 일치하지 않습니다.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user