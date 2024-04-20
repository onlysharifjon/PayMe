# Generated by Django 4.2.11 on 2024-04-20 11:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymeusers', '0006_alter_humocard_expired_alter_uzcard_expired_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymenthistory',
            name='money',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='humocard',
            name='expired',
            field=models.DateTimeField(default=datetime.datetime(2028, 4, 19, 11, 6, 25, 949953, tzinfo=datetime.timezone.utc), editable=False),
        ),
        migrations.AlterField(
            model_name='uzcard',
            name='expired',
            field=models.DateTimeField(default=datetime.datetime(2028, 4, 19, 11, 6, 25, 949953, tzinfo=datetime.timezone.utc), editable=False),
        ),
        migrations.AlterField(
            model_name='visaclassic',
            name='expired',
            field=models.DateTimeField(default=datetime.datetime(2028, 4, 19, 11, 6, 25, 949953, tzinfo=datetime.timezone.utc), editable=False),
        ),
        migrations.AlterField(
            model_name='visagold',
            name='expired',
            field=models.DateTimeField(default=datetime.datetime(2028, 4, 19, 11, 6, 25, 949953, tzinfo=datetime.timezone.utc), editable=False),
        ),
    ]
