from typing import operator

from django import forms as fforms
from django.contrib.auth import forms
from django.contrib.auth.forms import (AuthenticationForm, SetPasswordForm,
                                       UserChangeForm, UserCreationForm)
from django.forms import ModelForm, PasswordInput

from .models import Account


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Account


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Account
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            match = Account.objects.get(email=email)
        except Account.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('O email informado já se encontra cadastrado em nosso sistema.. Contate o administrador para mais informações.')


    def save(self, commit=True):
        '''
        Aqui eu posso tratar como os dados chegam após o formulário ser validado
        '''
        user = super(UserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name'].capitalize()
        user.last_name = self.cleaned_data["last_name"].capitalize()

        if commit:
            user.save()
        return user


    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome...'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Sobrenome...'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email...'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Senha...'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirmação de senha...'})


class LoginForm(ModelForm):
    '''Simple login form'''
    class Meta:
        model = Account
        fields = ('email', 'password')


    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email...'})
        self.fields['password'].widget = PasswordInput(attrs={'class': 'form-control', 'placeholder':'Senha...'})



class SetPasswordForm(forms.SetPasswordForm):
    class Meta(forms.SetPasswordForm):
        model = Account

    def __init__(self, *args, **kwargs):
        super(SetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': '...'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'pĺaceholder': '...'})



