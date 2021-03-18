from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..models import Tickets, Reply, Notification
from ..forms import NewTicket, EditTicket, TicketForm, ReplyForm
from django.conf import settings
from django.template.response import TemplateResponse


@login_required
def homePage(request, username):
    """
    A homepage deve conter todos tickets ativos do usuário e só.. manter o mais "clean" possível. 
    """
    table_open = []
    table_outdated = []
    table_closed = []

    tickets = Tickets.objects.filter(created_by=request.user, is_active=True).order_by('-created_at')
    for t in tickets:
        if t.status == "Pendente":
            table_open.append(t)
        elif t.status == "Em andamento":
            table_outdated.append(t)
        elif t.status == "Finalizado":
            table_closed.append(t)


    context = {
        "table_open": table_open, 
        "table_outdated": table_outdated, 
        "table_closed": table_closed,
        }
    return TemplateResponse(request, 'templates/home.html', context)

@login_required
def viewedTicket(request, id):
    instance = Notification.objects.get(id=id)
    instance.mark_as_read()
    ticket = Notification.objects.get(id=id)
    ticket_id = ticket.ticket.id
    Notification.turn_all_off()
    return redirect('ticket', id=ticket_id)
    


@login_required
def novoTicket(request, username):
    if request.method == 'POST':
        form = NewTicket(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.created_by = request.user
            new_form.save()
            return redirect('home', username=request.user.first_name)
    else:
        form = NewTicket()   

    context = {
        'form' : form
            }
    return TemplateResponse(request, 'templates/novoticket.html', context)


# Rever esse código
@login_required
def all_tickets(request, username):
    notifications = Notification()
    context = {
        'notifications': notifications.get_all(request.user),
    }
    return TemplateResponse(request, 'templates/all_tickets.html', context)


## Tickets Api's ##
@login_required
def deleteTicket(request, id):
    '''
    O ticket em si é inativado e não excluido.
    '''
    try:
        ticket = Tickets.objects.get(id=id)
        if ticket.created_by == request.user:
            ticket.is_active = False
            ticket.save()
        return redirect('home', username=request.user.first_name)
    except:
        print('Ticket not found')


@login_required
def editTicket(request, id):
    '''
    100%
    '''
    ticket = Tickets.objects.get(id=id)
    form = EditTicket(instance=ticket)
    if request.method == 'POST':
        form = EditTicket(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.save()
            return redirect('home', username=request.user.first_name)
    context = {
               'form' : form 
            }
    return TemplateResponse(request, 'templates/editticket.html', context)


@login_required
def verTicket(request, id):
    ticket = Tickets.objects.get(id=id)
    replies = Reply.objects.filter(ticket_id=id)
    
    form = ReplyForm()
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.ticket_id = id
            forms.owner_id = request.user.id
            forms.save()
            

    context = {'ticket': ticket,
               'replies': replies,
               'form': form
        }
    return TemplateResponse(request, 'templates/verticket.html', context)
