# Generated by Django 4.2.3 on 2023-08-28 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('course', models.TextField()),
                ('body', models.TextField()),
                ('genre', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]