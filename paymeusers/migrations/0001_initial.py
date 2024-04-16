# Generated by Django 5.0.3 on 2024-04-16 10:45

import datetime
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HumoCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(choices=[('uz_card', 'UzCard'), ('humo_card', 'HumoCard'), ('visa_classic', 'Visa Classic'), ('visa_gold', 'Visa Gold')], max_length=50)),
                ('number', models.CharField(max_length=16, unique=True)),
                ('pin_code', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(4), django.core.validators.MaxValueValidator(4)])),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expired', models.DateTimeField(default=datetime.datetime(2028, 4, 15, 10, 45, 7, 342705, tzinfo=datetime.timezone.utc), editable=False)),
                ('owner_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UzCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(choices=[('uz_card', 'UzCard'), ('humo_card', 'HumoCard'), ('visa_classic', 'Visa Classic'), ('visa_gold', 'Visa Gold')], max_length=50)),
                ('number', models.CharField(max_length=16, unique=True)),
                ('pin_code', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(4), django.core.validators.MaxValueValidator(4)])),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expired', models.DateTimeField(default=datetime.datetime(2028, 4, 15, 10, 45, 7, 342705, tzinfo=datetime.timezone.utc), editable=False)),
                ('owner_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VisaClassic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(choices=[('uz_card', 'UzCard'), ('humo_card', 'HumoCard'), ('visa_classic', 'Visa Classic'), ('visa_gold', 'Visa Gold')], max_length=50)),
                ('number', models.CharField(max_length=16, unique=True)),
                ('pin_code', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(4), django.core.validators.MaxValueValidator(4)])),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expired', models.DateTimeField(default=datetime.datetime(2028, 4, 15, 10, 45, 7, 342705, tzinfo=datetime.timezone.utc), editable=False)),
                ('owner_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VisaGold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(choices=[('uz_card', 'UzCard'), ('humo_card', 'HumoCard'), ('visa_classic', 'Visa Classic'), ('visa_gold', 'Visa Gold')], max_length=50)),
                ('number', models.CharField(max_length=16, unique=True)),
                ('pin_code', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(4), django.core.validators.MaxValueValidator(4)])),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expired', models.DateTimeField(default=datetime.datetime(2028, 4, 15, 10, 45, 7, 342705, tzinfo=datetime.timezone.utc), editable=False)),
                ('owner_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]