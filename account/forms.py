from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import forms
from .models import Account

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Account


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Account
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']


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

