from django.urls import path
from .views import *

urlpatterns = [
    path('all_user/', AllUser.as_view(), name='hamm userni database dan obkeberadi'),
    path('register/', RegisterAPI.as_view(), name='Regitstatsya qismi'),
    path('login/', LoginAPI.as_view(), name='login qismi'),
    path('add/card', AddCardAPI.as_view(), name='add card qismi'),
    path('all/card', AllCardAPI.as_view(), name='all card qismi'),
    path('all/his', AllHistoryPayment.as_view(),name = 'all history qismi'),
    path('search/card', SearchCardAPI.as_view(), name='search card qismi'),
    path('delete/card',DeleteCard.as_view(),name='kartani o`chirish'),
    path('delete/user',DeleteUser.as_view(),name='userni o`chirish'),
]
