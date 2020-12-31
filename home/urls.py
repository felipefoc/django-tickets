from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.homePage, name='home'),
    path('<str:username>/novoticket', views.novoTicket, name='novoTicket'),
]