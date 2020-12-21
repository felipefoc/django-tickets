from django.shortcuts import render
from .forms import UserCreationForm


# Create your views here.
def loginPage(request):
    context = {}
    return render(request, 'templates/login-page.html', context)


def registerPage(request):
    '''
    Criar registro dos usuários.. obs: Usuário é diferente de perfil.. após a criação do usuário é necessário criar um perfil para o mesmo
    '''
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        print('form validada')
        form.save()
        return redirect('loginPage')
    else:
        print('INVALIDA')
    context = {'form': form}
    return render(request, 'templates/register-page.html', context)