from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..models import Tickets, Reply, Notification
from ..forms import NewTicket, EditTicket, TicketForm, ReplyForm
from django.conf import settings
from django.utils import timezone
from django.core.paginator import Paginator
import sweetify as swal


@login_required
def homeOperator(request, username):
    tickets = Tickets.objects.filter(is_active=True).order_by('-created_at')

    tickets_open = []
    tickets_in_progress = []
    tickets_finished = []

    for i in tickets:
        if i.status == 'Pendente':
            tickets_open.append(i)
        if i.status == 'Em andamento':
            tickets_in_progress.append(i)
        if i.status == 'Finalizado':
            tickets_finished.append(i)


    context = {
        "tickets": tickets,
        "tickets_open": tickets_open,
        "tickets_in_progress": tickets_in_progress,
        "tickets_finished": tickets_finished,
    }
    return render(request, 'templates/operator/op_tickets.html', context)


@login_required
def openTicket(request, id):
    ticket = Tickets.objects.get(id=id)
    swal.success(request, title='Aberto', text="O Ticket agora está em andamento")
    ticket.status = 'Em andamento'
    ticket.operator = request.user
    ticket.operator_receive_date = timezone.localtime(timezone.now())
    ticket.save()

    notification = Notification.objects.create(
        text = 'Ticket de número {} foi aberto.'.format(ticket.id),
        ticket = ticket,
        owner = ticket.created_by
    )
    notification.save()


    return redirect('homeOperator', username=request.user.first_name )


@login_required
def closeTicket(request, id):
    ticket = Tickets.objects.get(id=id)
    ticket.status = 'Finalizado'
    ticket.ended_in = timezone.localtime(timezone.now())
    ticket.save()

    notification = Notification.objects.create(
        text = 'Ticket de número {} foi fechado pelo operador {}.'.format(ticket.id,
                                                                    ticket.operator),
        ticket = ticket,
        owner = ticket.created_by
    )
    notification.save()

    return redirect('homeOperator', username=request.user.first_name )


@login_required
def verTicketOperator(request, id):
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

            notification = Notification.objects.create(
                text = 'Nova resposta para o ticket {}.'.format(ticket.id),
                ticket = ticket,
                owner = ticket.created_by
            )
            notification.save()
            
    context = {'ticket': ticket,
               'replies': replies,
               'form': form,}
    return render(request, 'templates/verticket.html', context)
