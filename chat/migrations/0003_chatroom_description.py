# Generated by Django 3.1.1 on 2020-10-06 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20201006_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='description',
            field=models.CharField(default='Enter Your Room Description', max_length=500),
        ),
    ]
