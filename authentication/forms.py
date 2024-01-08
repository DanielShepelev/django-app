from django import forms
from authentication.models import FoodiUser
from django.contrib.auth.forms import AuthenticationForm



class UserForm(forms.ModelForm):

    class Meta:
        model = FoodiUser
        fields = ('username', 'email', 'password')
        exclude = ['confirm_password']

class UserAuthenticationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

        