from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from ..forms import CreateSector, EditTicket, NewTicket, ReplyForm, TicketForm, CreateType, AddOperator
from ..models import Reply, SectorType, Tickets, TicketType

from account.models import Account


def adminHome(request, username):
    all_tickets = Tickets.objects.all()
    all_operators = Account.objects.filter(is_operator=True)
    all_users = Account.objects.filter(is_operator=False, is_admin=False)
    table_open = []
    table_outdated = []
    table_closed = []
    
    tickets = Tickets.objects.filter(is_active=True)
    for t in tickets:
        if t.status == "Pendente":
            table_open.append(t)
        elif t.status == "Em andamento":
            table_outdated.append(t)
        elif t.status == "Finalizado":
            table_closed.append(t)
            
    context = {'all_tickets': all_tickets,
               'table_open': table_open,
               'table_outdated': table_outdated,
               'table_closed': table_closed,
               'all_operators': all_operators,
               'all_users': all_users,
                }
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


def createType(request, username):
    form = CreateType()
    if request.method == 'POST':
        form = CreateType(request.POST)
        if form.is_valid():
            form.save()    
    context = {'form': form }
    return render(request, 'templates/admin/create_type.html', context)


def removeType(request, id):
    sort = TicketType.objects.get(pk=id)
    sort.delete()
    return redirect('admin_sectors', username=request.user.first_name)


def operadorHome(request, username):
    all_operators = Account.objects.filter(is_operator=True)
    context = {'all_operators': all_operators }
    return render(request, 'templates/admin/adminOperators.html', context)


def addOperators(request, username):
    if request.method == 'POST':
        form = AddOperator(request.POST)
        if form.is_valid():
            pk = form.data['operators']
            operator = Account.objects.get(pk=pk)
            operator.is_operator = True
            operator.save()
        else:
            print(form.errors)
    else:
        form = AddOperator()
    context = {'form': form}
    return render(request, 'templates/admin/create_operator.html', context)
    
    
def removeOperator(request, id):
    operator = Account.objects.filter(id=id).first()
    operator.is_operator = False
    operator.save()
    username = request.user.first_name
    return redirect('addOperators', username=username)
    



"""
Testando criação de api
"""


def api_createRandomUser(request):
    if request.method == 'GET':
        import requests
        import json
        from django.http import JsonResponse
        from random import randint

        r = requests.get('https://randomuser.me/api/')

        r = r.json()

        f_name = r['results'][0]['name']['first']
        l_name = r['results'][0]['name']['last']
        email = r['results'][0]['email']
        password = r['results'][0]['login']['password'].capitalize() + '{}'.format(randint(10,20))

        response = {'f_name' : f_name,
                    'l_name' : l_name,
                    'email' : email,
                    'password' : password}

        return JsonResponse(response)
    else:
        pass
