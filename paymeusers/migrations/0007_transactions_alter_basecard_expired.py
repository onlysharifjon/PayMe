# Generated by Django 5.0.6 on 2024-05-21 10:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymeusers', '0006_bank_alter_basecard_expired'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=16)),
                ('getter', models.CharField(max_length=16)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('money', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='basecard',
            name='expired',
            field=models.DateTimeField(default=datetime.datetime(2028, 5, 20, 10, 45, 1, 675935, tzinfo=datetime.timezone.utc), editable=False),
        ),
    ]
