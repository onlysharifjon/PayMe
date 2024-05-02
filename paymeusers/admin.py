from django.contrib import admin
from .models import *

admin.site.register(UzCard, list_display=['id', 'number', 'owner_name', 'created', 'expired'])
admin.site.register(PaymentHistory, list_display=['who', 'where', 'time', 'money'])
admin.site.register(PaymeUser, list_display=['name', 'phone', 'password'])
