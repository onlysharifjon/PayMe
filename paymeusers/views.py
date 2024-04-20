from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.

from rest_framework.views import APIView
from .serializers import Tarjimon_Odamlar

from .models import User


class HammaOdamlar(APIView):
    def get(self, request):

        user = User.objects.all()
        serializer = Tarjimon_Odamlar(user,many=True)

        return Response(serializer.data)
