# Generated by Django 4.1.2 on 2022-11-16 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pro_club', '0012_alter_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='due',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member', to='pro_club.member'),
        ),
    ]