# Generated by Django 3.2.6 on 2021-08-28 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_profile_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]
