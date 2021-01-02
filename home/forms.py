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
            self.fields['imagem'].widget.attrs.update({'class': 'custom-file-input'})
            self.fields['imagem'].label = "Anexo de arquivos"
