# Generated by Django 5.0.6 on 2024-05-16 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymeusers', '0005_basecard_money_alter_basecard_expired'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='basecard',
            name='expired',
            field=models.DateTimeField(default=datetime.datetime(2028, 5, 15, 11, 10, 38, 78169, tzinfo=datetime.timezone.utc), editable=False),
        ),
    ]
