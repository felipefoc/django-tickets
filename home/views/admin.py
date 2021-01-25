from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..models import Tickets, Reply, SectorType
from ..forms import NewTicket, EditTicket, TicketForm, ReplyForm
from django.conf import settings


def adminHome(request, username):
    all_tickets = Tickets.objects.all()
    context = {}
    return render(request, 'templates/admin/adminhome.html', context)


def admin_sectors(request):
    all_sectors = SectorType.objects.all()
    context = { 'all_sectors': all_sectors }
    return render(request, 'templates/admin/adminSectors.html', context)