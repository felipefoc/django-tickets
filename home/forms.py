from django import forms
from .models import Tickets

class NewTicket(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ['tipo', 'setor', 'descrição', 'imagem']

    def __init__(self, *args, **kwargs):
            super(NewTicket, self).__init__(*args, **kwargs)
            self.fields['tipo'].widget.attrs.update({'class': 'form-control',
            'placeholder': '...'})
            self.fields['setor'].widget.attrs.update({'class': 'form-control',
            'placeholder': '...'})
            self.fields['descrição'].widget.attrs.update({'class': 'form-control',
             'placeholder': 'Qual o assunto do seu ticket ?', 'rows':'5',})
            self.fields['imagem'].widget.attrs.update({'class': 'custom-file-input', 'multiple': True})
            self.fields['imagem'].label = "Anexar arquivos"


class EditTicket(forms.ModelForm):
    class Meta:
        model = Tickets
        exclude = ['criado_por', 'status', 'is_active']


    def __init__(self, *args, **kwargs):
        super(EditTicket, self).__init__(*args, **kwargs)
        self.fields['tipo'].widget.attrs.update({'class': 'form-control',
            'placeholder': '...'})
        self.fields['setor'].widget.attrs.update({'class': 'form-control',
            'placeholder': '...'})
        self.fields['descrição'].widget.attrs.update({'class': 'form-control',
             'placeholder': 'Qual o assunto do seu ticket ?', 'rows':'5',})
        self.fields['imagem'].widget.attrs.update({'class': 'custom-file-input', 'multiple': True})
        self.fields['imagem'].label = "Anexar arquivos"


class TicketForm(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        
