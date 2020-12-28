from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserCreationForm, LoginForm


# Create your views here.
def loginPage(request):
    '''
    Página de login
    '''
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('home', username=user.first_name)

        else:
            messages.error(request, 'Nome de usuário e/ou senha incorreto')           
    context = {'form': form }
    return render(request, 'templates/login-page.html', context)


def registerPage(request):
    '''
    Página de Registro
    '''
    form = UserCreationForm()
    if request.method == 'POST': 
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'templates/register-page.html', context)




