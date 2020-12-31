from django.shortcuts import render, redirect
from .forms import NewTicket


# Create your views here.
def homePage(request, username):
    context = {'user' : request.user }
    return render(request, 'templates/home.html', context)


def novoTicket(request, username):
    form = NewTicket()

    if request.method == 'POST':
        form = NewTicket(request.POST)

    context = {'user' : request.user,
                'form' : form }
    return render(request, 'templates/novoticket.html', context)