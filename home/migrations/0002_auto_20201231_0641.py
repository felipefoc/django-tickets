# Generated by Django 3.1.4 on 2020-12-31 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='setor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.setorticket'),
        ),
        migrations.AddField(
            model_name='tickets',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.tipoticket'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='descrição',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='status',
            field=models.CharField(choices=[('Em andamento', 'Em andamento'), ('Finalizado', 'Finalizado'), ('Pendente', 'Pendente')], max_length=30, null=True),
        ),
    ]
