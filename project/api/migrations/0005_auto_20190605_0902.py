# Generated by Django 2.2.2 on 2019-06-05 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190605_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='booked_by',
            field=models.OneToOneField(default=None, on_delete=None, to='api.User'),
        ),
    ]