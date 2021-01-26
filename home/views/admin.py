from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from home.forms import CreateSector

from ..forms import CreateSector, EditTicket, NewTicket, ReplyForm, TicketForm
from ..models import Reply, SectorType, Tickets, TicketType


def adminHome(request, username):
    all_tickets = Tickets.objects.all()
    context = {}
    return render(request, 'templates/admin/adminhome.html', context)


def admin_sectors(request, username):
    all_sectors = SectorType.objects.all()
    all_sorts = TicketType.objects.all()
    context = { 'all_sectors': all_sectors,
                'all_sorts' : all_sorts, }
    return render(request, 'templates/admin/adminSectors.html', context)


def createSector(request, username):
    form = CreateSector()
    if request.method == 'POST':
        form = CreateSector(request.POST)
        if form.is_valid():
            form.save()    
    context = {'form': form }
    return render(request, 'templates/admin/create_sector.html', context)


def removeSector(request, id):
    sector = SectorType.objects.get(pk=id)
    sector.delete()
    return redirect('admin_sectors', username=request.user.first_name)