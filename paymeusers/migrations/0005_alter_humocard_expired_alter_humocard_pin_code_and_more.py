# Generated by Django 4.2.11 on 2024-04-20 10:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymeusers', '0004_alter_humocard_expired_alter_uzcard_expired_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humocard',
            name='expired',
            field=models.DateTimeField(default=datetime.datetime(2028, 4, 19, 10, 42, 2, 15389, tzinfo=datetime.timezone.utc), editable=False),
        ),
        migrations.AlterField(
            model_name='humocard',
            name='pin_code',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='uzcard',
            name='expired',
            field=models.DateTimeField(default=datetime.datetime(2028, 4, 19, 10, 42, 2, 15389, tzinfo=datetime.timezone.utc), editable=False),
        ),
        migrations.AlterField(
            model_name='uzcard',
            name='pin_code',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='visaclassic',
            name='expired',
            field=models.DateTimeField(default=datetime.datetime(2028, 4, 19, 10, 42, 2, 15389, tzinfo=datetime.timezone.utc), editable=False),
        ),
        migrations.AlterField(
            model_name='visaclassic',
            name='pin_code',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='visagold',
            name='expired',
            field=models.DateTimeField(default=datetime.datetime(2028, 4, 19, 10, 42, 2, 15389, tzinfo=datetime.timezone.utc), editable=False),
        ),
        migrations.AlterField(
            model_name='visagold',
            name='pin_code',
            field=models.CharField(max_length=4),
        ),
    ]
