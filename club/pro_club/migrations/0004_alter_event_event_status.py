# Generated by Django 4.1.2 on 2022-10-27 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro_club', '0003_alter_fund_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_status',
            field=models.CharField(blank=True, choices=[('COMPLETE', 'COMPLETE'), ('UPCOMMING', 'UPCOMMING')], default='UPCOMMING', max_length=20, null=True),
        ),
    ]
