from django import forms
from django.forms.models import model_to_dict
from django.forms.widgets import CheckboxSelectMultiple

from home.models import Account, SectorType, TicketType

from .models import OperatorAccount, Tickets


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
        exclude = ['created_by', 'status', 'is_active', 'operator_receive_date', 'ended_in']


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
         

class OperatorSettings(forms.ModelForm):
    class Meta():
        model = OperatorAccount
        fields = ('sector1', 'sort1', 'operator')

    sector1 = forms.ModelMultipleChoiceField(
        queryset = SectorType.objects.filter(status=True),
        widget  = forms.CheckboxSelectMultiple,
        label = 'Setor',
    )

    sort1 = forms.ModelMultipleChoiceField(
        queryset = TicketType.objects.filter(status=True),
        widget  = forms.CheckboxSelectMultiple,
        label = 'Tipo :',
    )


    def __init__(self, *args, **kwargs):
        super(OperatorSettings, self).__init__(*args, **kwargs)
        #self.fields['sector'].label = 'Setores :'
        #self.fields['sort'].label = 'Tipos :'
        self.fields['operator'].label = 'Operador :'
        self.fields['operator'].queryset = Account.objects.filter(is_operator=True)
