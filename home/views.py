from django.shortcuts import render, redirect


# Create your views here.
def homePage(request, username):
    context = {'user' : request.user }
    return render(request, 'templates/base_home.html', context)