# Generated by Django 3.0.8 on 2020-09-12 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('nickname', models.CharField(default=models.CharField(max_length=255, unique=True), max_length=124, unique=True)),
            ],
        ),
    ]
