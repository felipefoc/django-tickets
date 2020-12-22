from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/home/', views.homePage, name='home'),  
]