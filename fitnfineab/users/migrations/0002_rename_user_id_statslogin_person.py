# Generated by Django 3.2.8 on 2021-12-01 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statslogin',
            old_name='user_id',
            new_name='person',
        ),
    ]