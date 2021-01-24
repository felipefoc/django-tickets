from django import forms
from django.forms.models import model_to_dict
from django.forms.widgets import CheckboxSelectMultiple

from home.models import Account, SectorType, TicketType

from .models import Tickets, Reply


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
        fields = ['text',]

    def __init__(self, *args, **kwargs):
        super(ReplyForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-control',
            'placeholder': 'Digite a resposta do ticket...'})
        self.fields['text'].label = 'Resposta :'
    
