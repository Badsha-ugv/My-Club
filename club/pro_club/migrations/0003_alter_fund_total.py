# Generated by Django 4.1.2 on 2022-10-27 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro_club', '0002_alter_payment_due_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]