from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('login/', views.loginPage, name='login'),
    path('registrar/', views.registerPage, name='register'),    
]
