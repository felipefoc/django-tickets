from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('<str:username>/PaginaInicial', views.homePage, name='home'),
    path('Operador/<str:username>/', views.homeOperator, name='homeOperator'),
    path('Operador/AbrirTicket<int:id>', views.openTicket, name='openTicket'),
    path('<str:username>/novoticket', views.novoTicket, name='novoTicket'),
    path('DeleteTicket/<int:id>', views.deleteTicket, name='deleteticket'),
    path('EditTicket/<int:id>', views.editTicket, name='editticket'),
    path('Ticket<int:id>', views.verTicket, name='ticket'),
    path('TicketOperator<int:id>', views.verTicketOperator, name='verTicketOperator'),
    path('<str:username>_ADMIN/', views.adminHome, name='adminhome'),
    path('Setores/', views.admin_sectors, name='admin_sector'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
