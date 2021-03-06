# Generated by Django 3.2 on 2022-04-03 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_item_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='completed',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='order',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='item',
            name='url',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
