from django.contrib import admin
from .models import *

# admin.site.register(UzCard, list_display=['id', 'number', 'owner_name', 'created', 'expired'])
admin.site.register(PaymentHistory, list_display=['who', 'where', 'time', 'money'])
admin.site.register(PaymeUser, list_display=['name', 'phone', 'password'])
admin.site.register(BaseCard, list_display=['card_type', 'number', 'owner_name', 'is_active', 'expired'])
admin.site.register(Bank, list_display=['money', 'name'])


class TransactionsAdmin(admin.ModelAdmin):
    search_fields = ('sender',)
    list_display = ['sender', 'getter', 'time', 'money']


admin.site.register(Transactions, TransactionsAdmin, )
