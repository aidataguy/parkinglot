# Generated by Django 2.2.2 on 2019-06-05 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190605_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='parking',
            name='booked_by',
            field=models.OneToOneField(default=None, on_delete=None, to='api.User'),
        ),
    ]