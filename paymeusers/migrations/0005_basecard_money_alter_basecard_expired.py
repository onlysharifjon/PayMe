# Generated by Django 5.0.6 on 2024-05-14 11:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymeusers', '0004_alter_basecard_expired'),
    ]

    operations = [
        migrations.AddField(
            model_name='basecard',
            name='money',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basecard',
            name='expired',
            field=models.DateTimeField(default=datetime.datetime(2028, 5, 13, 11, 20, 9, 756110, tzinfo=datetime.timezone.utc), editable=False),
        ),
    ]
