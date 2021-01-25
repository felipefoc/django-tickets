from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout as django_logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserCreationForm, LoginForm, SetPasswordForm
from account.presenters.loginPagePresenter import LoginPagePresenter

# Create your views here.
def loginPage(request):
    '''
    Página de login
    '''
    userIsActiveAndAuthenticated = LoginPagePresenter.userAuthenticatedAndActivaded(request)
    requestIsPost = LoginPagePresenter.requestIsPost(request, authenticate, login, messages)
    if userIsActiveAndAuthenticated != None:
        return redirect(userIsActiveAndAuthenticated[0], userIsActiveAndAuthenticated[1])

    form = LoginForm()
    context = {'form': form }
    return render(requestIsPost[0],requestIsPost[1],requestIsPost[2])


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




