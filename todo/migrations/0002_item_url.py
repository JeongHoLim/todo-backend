# Generated by Django 3.2 on 2022-04-03 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='url',
            field=models.CharField(default='http://localhost:8080/', max_length=1000),
        ),
    ]
