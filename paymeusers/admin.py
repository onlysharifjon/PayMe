from django.contrib import admin
# Register your models here.

from .models import UzCard, HumoCard, VisaGold, VisaClassic


@admin.register(UzCard)
class UzCardAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'owner_name', 'created', 'expired']

#
# @admin.register(HumoCard)
# class HumoCardAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(VisaGold)
# class VisaGoldAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(VisaClassic)
# class VisaClassicAdmin(admin.ModelAdmin):
#     pass
