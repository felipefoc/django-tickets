# Generated by Django 3.1.4 on 2020-12-31 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201231_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='imagem',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
    ]
