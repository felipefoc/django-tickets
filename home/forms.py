from django import forms
from .models import Tickets

class NewTicket(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ['_type', 'sector', 'description', 'files']

    def __init__(self, *args, **kwargs):
            super(NewTicket, self).__init__(*args, **kwargs)
            self.fields['_type'].widget.attrs.update({'class': 'form-control',
            'placeholder': '...'})
            self.fields['sector'].widget.attrs.update({'class': 'form-control',
            'placeholder': '...'})
            self.fields['description'].widget.attrs.update({'class': 'form-control',
             'placeholder': 'Qual o assunto do seu ticket ?', 'rows':'5',})
            self.fields['files'].widget.attrs.update({'class': 'custom-files-input', 'multiple': True})
            self.fields['files'].label = "Anexar arquivos"


class EditTicket(forms.ModelForm):
    class Meta:
        model = Tickets
        exclude = ['created_by', 'status', 'is_active']


    def __init__(self, *args, **kwargs):
        super(EditTicket, self).__init__(*args, **kwargs)
        self.fields['_type'].widget.attrs.update({'class': 'form-control',
            'placeholder': '...'})
        self.fields['sector'].widget.attrs.update({'class': 'form-control',
            'placeholder': '...'})
        self.fields['description'].widget.attrs.update({'class': 'form-control',
             'placeholder': 'Qual o assunto do seu ticket ?', 'rows':'5',})
        self.fields['files'].widget.attrs.update({'class': 'custom-files-input', 'multiple': True})
        self.fields['files'].label = "Anexar arquivos"


class TicketForm(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
         
