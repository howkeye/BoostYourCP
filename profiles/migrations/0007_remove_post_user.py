# Generated by Django 2.2.5 on 2020-02-01 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]
