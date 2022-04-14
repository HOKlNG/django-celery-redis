from django import forms
from app_accounts.models import User
from django.contrib.auth.hashers import check_password, make_password


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

class LoginForm(forms.Form):

    email = forms.CharField(
        error_messages={'required': '이메일을 입력해주세요'},
        max_length=128,
        label='이메일',
        widget=forms.EmailInput(attrs={'placeholder': '이메일을 입력해주세요', 'data-width': '100%'})
    )
    password = forms.CharField(
        error_messages={'required': "비밀번호를 입력해주세요"},
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호를 입력해주세요', 'data-width': '100%'}),
        label="비밀번호",
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                self.add_error('user_id', '아이디가 없습니다.')
                return

            if not check_password(password, user.password):
                self.add_error('password', '비밀번호를 틀렸습니다.')
