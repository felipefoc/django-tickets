from django.shortcuts import render

# Create your views here.
def loginPage(request):
    context = {}
    return render(request, 'templates/login-page.html', context)


def registerPage(request):
    context = {}
    return render(request, 'templates/register-page.html', context)