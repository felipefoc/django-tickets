from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Tickets
from .forms import NewTicket
from time import sleep
from django.conf import settings
import random, string


# Create your views here.
def homePage(request, username):
    formopen = Tickets.objects.filter(criado_por=request.user, is_active=True)
    context = {'user' : request.user,
               'form': formopen,}
    return render(request, 'templates/home.html', context)


def novoTicket(request, username):
    form = NewTicket()

    if request.method == 'POST':
        form = NewTicket(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.criado_por = request.user
            filename = ''.join(random.choice(string.ascii_letters) for _ in range(3))
            new_form.imagem.field.upload_to = f'user_{request.user.id}/{filename}'
            new_form.save()
            return redirect('home', username=request.user.first_name )
        else:
            print('Form isnt valid')

    context = {'user' : request.user,
                'form' : form }
    return render(request, 'templates/novoticket.html', context)

## Tickets Api's ##
def deleteTicket(request, id):
    '''
    O ticket em si é inativado e não excluido.
    '''
    try:
        ticket = Tickets.objects.filter(id=id).first()
        if ticket.criado_por == request.user:
            ticket.is_active = False
            ticket.save()
        return redirect('home', username=request.user.first_name )
    except:
        print('Ticket not found')

def editTicket(request, id):
    '''
    TODO FIX THIS !
    '''
    try:
        ticket = Tickets.objects.filter(id=id).first()
    except:
        pass
    data = {
        'tipo' : ticket.tipo,
        'setor' : ticket.setor,
        'descrição' : ticket.descrição,
        'imagem' : ticket.imagem,
        'criado_em' : ticket.criado_em,
        'cirado_por' : ticket.criado_por
    }
    form = NewTicket(initial=data)
    if request.method == 'POST':
        form = NewTicket(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            filename = ''.join(random.choice(string.ascii_letters) for _ in range(3))
            new_form.imagem.field.upload_to = f'user_{request.user.id}/{filename}'
            new_form.save()
            return redirect('home', username=request.user.first_name )

    context = {'user' : request.user,
               'form' : form }
    return render(request, 'templates/novoticket.html', context)
