from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..models import Tickets, Reply
from ..forms import NewTicket, EditTicket, TicketForm, ReplyForm
from django.conf import settings
from django.utils import timezone


@login_required
def homeOperator(request, username):
    tickets = Tickets.objects.filter(is_active=True).order_by('-created_at')
    context = {
        "tickets": tickets,
        }
    return render(request, 'templates/operator_template.html', context)


@login_required
def openTicket(request, id):
    ticket = Tickets.objects.filter(id=id).first()
    ticket.status = 'Em andamento'
    ticket.operator = request.user
    ticket.operator_receive_date = timezone.now()
    ticket.save()
    return redirect('homeOperator', username=request.user.first_name )


@login_required
def verTicketOperator(request, id):
    ticket = Tickets.objects.filter(id=id).first()
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
               'form': form,}
    return render(request, 'templates/verticket.html', context)
