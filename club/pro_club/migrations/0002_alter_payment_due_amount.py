# Generated by Django 4.1.2 on 2022-10-27 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro_club', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='due_amount',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
