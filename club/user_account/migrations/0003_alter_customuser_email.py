# Generated by Django 4.1.2 on 2022-11-03 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0002_customuser_club_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=40, null=True),
        ),
    ]