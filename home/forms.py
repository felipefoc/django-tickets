from django import forms
from .models import Tickets

class NewTicket(forms.ModelForm):

    class Meta:
        model = Tickets
        fields = ['tipo', 'setor', 'descrição', ]


