# Generated by Django 4.1.2 on 2022-11-07 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0004_alter_customuser_gender_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='student_id',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]