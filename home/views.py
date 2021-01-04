from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Tickets
from .forms import NewTicket, EditTicket
from django.conf import settings
import random, string



# Create your views here.
@login_required
def homePage(request, username):
    '''
    A homepage deve contêr todos tickets ativos do usuário e só.. manter o mais "clean" possível. 
    '''
    formopen = Tickets.objects.filter(criado_por=request.user, is_active=True, status='Pendente').order_by('-criado_em') # Tickets em aberto
    formclosed = Tickets.objects.filter(criado_por=request.user, is_active=True, status='Finalizado').order_by('-criado_em') # Tickets finalizados
    formstarted = Tickets.objects.filter(criado_por=request.user, is_active=True, status='Em andamento').order_by('-criado_em') # Tickets em andamento
    context = {'user' : request.user,
               'formopen': formopen,
               'formclosed': formclosed,
               'formstarted' :formstarted }
    return render(request, 'templates/home.html', context)


@login_required
def novoTicket(request, username):
    if request.method == 'POST':
        form = NewTicket(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.criado_por = request.user
            filename = ''.join(random.choice(string.ascii_letters) for _ in range(5)) 
            new_form.imagem.field.upload_to = f'user_{request.user.id}/{filename}'
            new_form.save()
            return redirect('home', username=request.user.first_name )
    else:
        form = NewTicket()   

    context = {'user' : request.user,
                'form' : form }
    return render(request, 'templates/novoticket.html', context)

## Tickets Api's ##
@login_required
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


@login_required
def editTicket(request, id):
    '''
    100%
    '''
    ticket = Tickets.objects.filter(id=id).first()
    form = EditTicket(instance=ticket)
    if request.method == 'POST':
        form = EditTicket(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            new_form = form.save(commit=False)
            filename = ''.join(random.choice(string.ascii_letters) for _ in range(5))
            new_form.imagem.field.upload_to = f'user_{request.user.id}/{filename}'
            new_form.save()
            return redirect('home', username=request.user.first_name )

    context = {'user' : request.user,
               'form' : form }
    return render(request, 'templates/editticket.html', context)
