# Generated by Django 3.1.4 on 2021-01-12 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='operator_receive_date',
            field=models.DateTimeField(null=True),
        ),
    ]