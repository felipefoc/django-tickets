# Generated by Django 3.1.4 on 2021-01-24 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_delete_coreply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.tickets'),
        ),
    ]
