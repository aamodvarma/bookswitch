# Generated by Django 3.2.6 on 2021-08-12 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210812_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='product',
            name='uploadid',
        ),
    ]
