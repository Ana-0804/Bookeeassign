# Generated by Django 4.2 on 2023-10-23 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorisation', '0003_alter_client_user_alter_trainer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
