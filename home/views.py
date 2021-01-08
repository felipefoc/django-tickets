from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Tickets
from .forms import NewTicket, EditTicket, TicketForm
from django.conf import settings
import random, string



# Create your views here.
@login_required
def homePage(request, username):
    '''
    A homepage deve conter todos tickets ativos do usuário e só.. manter o mais "clean" possível. 
    '''
    tickets = Tickets.objects.filter(created_by=request.user, is_active=True).order_by('-created_at') # Tickets em aberto
    context = {'user' : request.user,
               'tickets': tickets }
    return render(request, 'templates/home.html', context)


@login_required
def novoTicket(request, username):
    if request.method == 'POST':
        form = NewTicket(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.created_by = request.user
            filename = ''.join(random.choice(string.ascii_letters) for _ in range(5)) 
            new_form.image.field.upload_to = f'user_{request.user.id}/{filename}'
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
        if ticket.created_by == request.user:
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
            #new_form.image.field.upload_to = f'user_{request.user.id}/{filename}'
            new_form.save()
            return redirect('home', username=request.user.first_name )

    context = {'user' : request.user,
               'form' : form }
    return render(request, 'templates/editticket.html', context)


def verTicket(request, username, id):
    ticket = Tickets.objects.filter(id=id).first()
    context = {'ticket': ticket }
    return render(request, 'templates/verticket.html', context)
