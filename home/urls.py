from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.homePage, name='home'),
    path('<str:username>/novoticket', views.novoTicket, name='novoTicket'),
    path('DeleteTicket/<int:id>', views.deleteTicket, name='deleteticket'),
    path('EditTicket/<int:id>', views.editTicket, name='editticket'),
    path('<str:username>/Ticket<int:id>', views.verTicket, name='ticket'),
]
