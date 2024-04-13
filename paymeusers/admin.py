from django.contrib import admin
# Register your models here.

from .models import UzCard, HumoCard, VisaGold, VisaClassic


@admin.register(UzCard)
class UzCardAdmin(admin.ModelAdmin):
    list_display = ['__all__']


@admin.register(HumoCard)
class HumoCardAdmin(admin.ModelAdmin):
    list_display = ['__all__']


@admin.register(VisaGold)
class VisaGoldAdmin(admin.ModelAdmin):
    list_display = ['__all__']


@admin.register(VisaClassic)
class VisaClassicAdmin(admin.ModelAdmin):
    list_display = ['__all__']
