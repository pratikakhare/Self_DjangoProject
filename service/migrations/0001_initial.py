# Generated by Django 5.0.2 on 2025-03-18 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('help_id', models.CharField(max_length=50)),
                ('help_title', models.CharField(max_length=50)),
                ('help_des', models.TextField()),
            ],
        ),
    ]
