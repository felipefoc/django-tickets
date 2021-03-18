from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('<str:username>/PaginaInicial', views.homePage, name='home'),
    path('Operador/<str:username>/', views.homeOperator, name='homeOperator'),
    path('Operador/AbrirTicket/id=<int:id>', views.openTicket, name='openTicket'),
    path('Operador/FecharTicket/id=<int:id>', views.closeTicket, name='closeTicket'),
    path('<str:username>/novoticket', views.novoTicket, name='novoTicket'),
    path('DeleteTicket/<int:id>', views.deleteTicket, name='deleteticket'),
    path('EditTicket/<int:id>', views.editTicket, name='editticket'),
    path('Ticket<int:id>', views.verTicket, name='ticket'),
    path('TicketOperator<int:id>', views.verTicketOperator, name='verTicketOperator'),
    path('<str:username>_ADMIN/', views.adminHome, name='adminHome'),
    path('<str:username>_ADMIN/Setores', views.admin_sectors, name='admin_sectors'),
    path('<str:username>_ADMIN/Setores/CriarSetor', views.createSector, name='createSector'),
    path('RemoverSetor/<int:id>', views.removeSector, name='removeSector'),
    path('<str:username>_ADMIN/Setores/CriarTipo', views.createType, name='createType'),
    path('RemoverTipo/<int:id>', views.removeType, name='removeType'),
    path('<str:username>_ADMIN/Operadores', views.operadorHome, name='operadorHome'),
    path('<str:username>_ADMIN/Operadores/AdicionarOperador', views.addOperators, name='addOperators'),
    path('RemoverOperador/<int:id>', views.removeOperator, name='removeOperator'),
    path('notify_ticket/<int:id>', views.viewedTicket, name='notify_ticket'),
    path('<str:username>/Notificacoes', views.all_tickets, name='all_tickets'),


    # API
    path('api_createRandomUser/', views.api_createRandomUser, name='api_createRandomUser'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
