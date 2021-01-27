from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from django.core.exceptions import ValidationError
from .models import Account, Reply, SectorType, Tickets, TicketType



class NewTicket(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ['sort', 'sector', 'description', 'files']

    def __init__(self, *args, **kwargs):
            super(NewTicket, self).__init__(*args, **kwargs)
            self.fields['sort'].widget.attrs.update({'class': 'form-control',
            'placeholder': '...'})
            self.fields['sort'].label = 'Tipo'
            self.fields['sector'].widget.attrs.update({'class': 'form-control',
            'placeholder': '...'})
            self.fields['sector'].label = 'Setor'
            self.fields['description'].widget.attrs.update({'class': 'form-control',
             'placeholder': 'Qual o assunto do seu ticket ?', 'rows':'5',})
            self.fields['description'].label = 'Descrição'
            self.fields['files'].widget.attrs.update({'class': 'custom-files-input', 'multiple': True})
            self.fields['files'].label = "Anexar arquivos"


class EditTicket(forms.ModelForm):
    class Meta:
        model = Tickets
        exclude = ['created_by', 'status', 'is_active', 'operator_receive_date', 'ended_in', 'operator']


    def __init__(self, *args, **kwargs):
        super(EditTicket, self).__init__(*args, **kwargs)
        self.fields['sort'].widget.attrs.update({'class': 'form-control',
            'placeholder': '...'})
        self.fields['sort'].label = 'Tipo'
        self.fields['sector'].widget.attrs.update({'class': 'form-control',
            'placeholder': '...'})
        self.fields['sector'].label = 'Setor'
        self.fields['description'].widget.attrs.update({'class': 'form-control',
            'placeholder': 'Qual o assunto do seu ticket ?', 'rows':'5',})
        self.fields['description'].label = 'Descrição'    
        self.fields['files'].widget.attrs.update({'class': 'custom-files-input', 'multiple': True})
        self.fields['files'].label = "Anexar arquivos"


class TicketForm(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
         

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['text']


    def __init__(self, *args, **kwargs):
        super(ReplyForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-control',
            'placeholder': 'Digite a resposta do ticket...'})
        self.fields['text'].label = 'Resposta :'


class CreateSector(forms.ModelForm):
    class Meta:
        model = SectorType
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(CreateSector, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Insira o nome do setor :'
        self.fields['name'].widget.attrs.update({'class': 'form-control'})


class CreateType(forms.ModelForm):
    class Meta:
        model = TicketType
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(CreateType, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Insira o nome do Tipo :'
        self.fields['name'].widget.attrs.update({'class': 'form-control'})


class AddOperator(forms.Form):
    operators = forms.ModelChoiceField(queryset=Account.objects.filter(is_operator=False))

    class Meta:
        model = Account
        fields = ['operators']

    def is_valid(self):
        valid = True
        if self.data['operators']:
            pk = self.data['operators']
            user_exists = Account.objects.filter(pk=pk).first()
            if user_exists and user_exists.is_admin == True:
                valid = False
                self.add_error('operators', 'DEU RUIM')
            return self.cleaned_data

    
