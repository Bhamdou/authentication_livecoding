from django import forms


class LoginForm(forms.Form):
    # username and password
    username = forms.CharField(label='Username', max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())