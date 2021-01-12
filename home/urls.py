from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('<str:username>/', views.homePage, name='home'),
    path('<str:username>/novoticket', views.novoTicket, name='novoTicket'),
    path('DeleteTicket/<int:id>', views.deleteTicket, name='deleteticket'),
    path('EditTicket/<int:id>', views.editTicket, name='editticket'),
    path('Ticket<int:id>', views.verTicket, name='ticket'),
    path('<str:username>/Operador', views.settingsOperator, name='settings_operator'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
