# Generated by Django 2.2.6 on 2019-10-31 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0003_libro'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha Creacion'),
        ),
    ]
