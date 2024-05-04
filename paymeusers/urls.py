from django.urls import path
from .views import *

urlpatterns = [
    path('all_user/', AllUser.as_view(), name='hamm userni database dan obkeberadi'),
    path('register/', RegisterAPI.as_view(), name='Regitstatsya qismi'),
    path('login/', LoginAPI.as_view(), name='login qismi'),
    path('add/card', AddCardAPI.as_view(), name='add card qismi'),
]
