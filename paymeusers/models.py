from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

from django.db import models
from datetime import timedelta


# Create your models here.
class BaseCard(models.Model):
    CARD_TYPES = [
        ('uz_card', 'UzCard'),
        ('humo_card', 'HumoCard'),
        ('visa_classic', 'Visa Classic'),
        ('visa_gold', 'Visa Gold')
    ]
    card_type = models.CharField(max_length=50, choices=CARD_TYPES)
    number = models.CharField(max_length=16, unique=True)
    # pin_code = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999)])
    pin_code = models.CharField(max_length=4)
    owner_name = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    expired = models.DateTimeField(default=timezone.now() + timedelta(days=365 * 4), editable=False)

    class Meta:
        abstract = True


class UzCard(BaseCard):
    def  __str__(self):
        return self.number


class HumoCard(BaseCard):
    pass


class VisaGold(BaseCard):
    pass


class VisaClassic(BaseCard):
    pass


class PaymentHistory(models.Model):
    who = models.ForeignKey(User,on_delete=models.CASCADE)
    CHOISE = (
        ('Taksi','Taksi'),
        ('Oziq-ovqat','Oziq-ovqat'),
        ('Texnika','Texnika'),
        ('O`tkazmalar','O`tkazmalar'),
        ('Kiyim','Kiyim'),
        ('Transport','Transport'),
        ('Komunal-To`lovlar','Komunal-To`lovlar'),
        ('Internet-Xizmatlari','Internet-Xizmatlari'),
        ('Telefoniya','Telefoniya'),
        ('Ta`lim','Ta`lim'),
        ('Jarimalar','Jarimalar'),
        ('Madaniy-Hordiq','Madaniy-Hordiq'),
        ('Xayriya-Fondlari','Xayriya-Fondlari'),
        ('Dorixona','Dorixona'),
        ('Boshqalar','Boshqalar'),
        ('Soliqlar','Soliqlar'),
        ('Notarius','Notarius'),
        ('Kredit','Kredit')
        )
    where = models.CharField(choices=CHOISE,max_length=40)
    time = models.DateTimeField(auto_now_add=True)
    money = models.IntegerField(default=0)
    def __str__(self) -> str:
        return str(self.who)

    