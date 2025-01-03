# Generated by Django 5.1.2 on 2024-12-25 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileobjapp', '0004_alter_client_filepath_alter_client_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='filepath',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(default='default_name', max_length=50, unique=True),
        ),
    ]
