from django.urls import path
from .views import HammaOdamlar

urlpatterns = [
    path('hamma/', HammaOdamlar.as_view())

]
