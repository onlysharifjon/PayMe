from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PaymeUser
from .serializers import QiynSerializer, OsonSerializer


class AllUser(APIView):
    def get(self, request):
        print(request)
        hamma_odamlar = PaymeUser.objects.all()
        serializer = OsonSerializer(hamma_odamlar, many=True)
        return Response(serializer.data, status=200)

class RegisterAPI(APIView):
    serializer_class = OsonSerializer

    def post(self, request):
        serializer = OsonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Xabar': "User Registratsiyadan o`tdi"}, status=200)
        else:
            return Response(serializer.errors, status=400)
class LoginAPI(APIView):
    serializer_class = QiynSerializer
    def post(self, request):
        phone_front = request.data.get('phone')
        password_front = request.data.get('password')

        filtr = PaymeUser.objects.all().filter(phone=phone_front, password=password_front)
        if filtr:
            serializer = OsonSerializer(filtr,many=True)
            return Response(serializer.data, status=200)
        else:
            return Response({'Xabar': 'Bunday Foydalanuvchi Bizda Mavjud emas'}, status=400)