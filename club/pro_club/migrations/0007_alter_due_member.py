# Generated by Django 4.1.2 on 2022-10-28 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pro_club', '0006_remove_due_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='due',
            name='member',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pro_club.member'),
        ),
    ]
