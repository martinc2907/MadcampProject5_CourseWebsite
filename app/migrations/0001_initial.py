# Generated by Django 2.0.1 on 2018-01-23 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=1000)),
                ('specialty', models.CharField(max_length=500)),
                ('github', models.CharField(max_length=500)),
                ('quote', models.CharField(max_length=500)),
                ('session', models.CharField(max_length=20)),
            ],
        ),
    ]