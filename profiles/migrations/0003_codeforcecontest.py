# Generated by Django 2.2.5 on 2020-01-31 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_codechefcontest'),
    ]

    operations = [
        migrations.CreateModel(
            name='codeforceContest',
            fields=[
                ('title', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('start', models.CharField(max_length=50)),
                ('end', models.CharField(max_length=50)),
            ],
        ),
    ]
