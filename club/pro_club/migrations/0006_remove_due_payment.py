# Generated by Django 4.1.2 on 2022-10-28 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_club', '0005_due'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='due',
            name='payment',
        ),
    ]
