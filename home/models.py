from django.db import models
from account.models import Account
from django.conf import settings

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
    def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
        return 'user_{0}/{1}'.format(instance.user.id, filename)

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


class CoReply(models.Model):
    text = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE)
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE)


'''
Não consegui deixar essa classe no Account por conta de 'CircularImport' 
'''
class OperatorAccount(models.Model):
    operator = models.ForeignKey(Account, on_delete=models.CASCADE)
    sort = models.ManyToManyField(TicketType)
    sector = models.ManyToManyField(SectorType)
    