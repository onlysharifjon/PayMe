from django.urls import path
from .views import *

urlpatterns = [
    path('all_user/', AllUser.as_view(), name='hamm userni database dan obkeberadi'),
    path('register/', RegisterAPI.as_view(), name='Regitstatsya qismi'),
    path('login/', LoginAPI.as_view(), name='login qismi'),
    path('add/card', AddCardAPI.as_view(), name='add card qismi'),
    path('all/card', AllCardAPI.as_view(), name='all card qismi'),
    path('all/his', AllHistoryPayment.as_view(), name='all history qismi'),
    path('search/card', SearchCardAPI.as_view(), name='search card qismi'),
    path('delete/card', DeleteCard.as_view(), name='kartani o`chirish'),
    path('delete/user', DeleteUser.as_view(), name='userni o`chirish'),
    path('change/password', ChangePassword.as_view(), name='parolni o`zgartirish'),
    path('transaction/', Transaction.as_view(), name='tranzaktsiya qilish'),
    path('user/id/<int:id>', SearchUser.as_view()),
    path('top/money/', SortedMoney.as_view(), name='Rating pul bo`yicha saralash'),
    path('searcher/', SearchByNumber.as_view()),
    path('top/transtaction/', TopMonthTransactionUser.as_view())
]
