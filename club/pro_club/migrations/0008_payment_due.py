# Generated by Django 4.1.2 on 2022-11-15 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pro_club', '0007_alter_due_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='due',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pro_club.due'),
        ),
    ]