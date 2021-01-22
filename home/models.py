from django.conf import settings
from django.db import models
from django.db.models import functions
from django.utils import timezone

from account.models import Account

# Create your models here.
class TicketType(models.Model):
    name = models.CharField(max_length=30)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class SectorType(models.Model):
    name = models.CharField(max_length=30)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Tickets(models.Model):
    def user_directory_path(self, instance, **kwargs):
        extension = instance.split('.')[-1]
        filename = f"arquivo_{timezone.now().strftime('%d%m%Y%H%M%S')}.{extension}"
        return 'user_{0}/{1}'.format(self.created_by.id, filename)

    CHOICES = (
        ('Em andamento', 'Em andamento'),
        ('Finalizado', 'Finalizado'),
        ('Pendente', 'Pendente'),
        )

    sort = models.ForeignKey(TicketType, null=True, on_delete=models.CASCADE)
    sector = models.ForeignKey(SectorType, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    modified_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30, choices=CHOICES, default='Pendente', blank=False, null=False)
    description = models.TextField(null=True)
    operator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                null=True, related_name='operator')
    operator_receive_date = models.DateTimeField(null=True)
    ended_in = models.DateTimeField(null=True)
    files = models.FileField(upload_to=user_directory_path , max_length=5000,
                             null=True, blank=True)
    is_active = models.BooleanField(default=True)


class Reply(models.Model):
    text = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE)

