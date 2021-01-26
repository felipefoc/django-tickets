from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout as django_logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserCreationForm, LoginForm, SetPasswordForm


# Create your views here.
def loginPage(request):
    '''
    Página de login
    '''
    if request.user.is_authenticated and request.user.is_active:
        if request.user.is_operator:
            return redirect('homeOperator', username=request.user.first_name)
        elif request.user.is_admin:
            return redirect('adminHome', username=request.user.first_name)
        return redirect('home', username=request.user.first_name)
   

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None and user.is_active:
            login(request, user)
            if user.is_operator:
                return redirect('homeOperator', username=user.first_name)
            elif request.user.is_admin:
                return redirect('adminHome', username=request.user.first_name)
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


@login_required
def changePassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)      
                return HttpResponseRedirect('/{}'.format(request.user.first_name))           
        else:
            form = SetPasswordForm(request.user) 
            print(form) 
    context = {'form': form }
    return render(request, 'templates/changepassword.html', context)

@login_required
def logout(request):
    django_logout(request)
    return redirect('login')
