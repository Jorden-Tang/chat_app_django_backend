# Generated by Django 3.1.1 on 2020-09-30 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatroom',
            old_name='room_name',
            new_name='name',
        ),
    ]
