from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from drf_yasg.utils import swagger_auto_schema


class AllUser(APIView):
    def get(self, request):
        print(request)
        hamma_odamlar = PaymeUser.objects.all()
        serializer = OsonSerializer(hamma_odamlar, many=True)
        return Response(serializer.data, status=200)


class RegisterAPI(APIView):
    serializer_class = OsonSerializer

    @swagger_auto_schema(request_body=OsonSerializer)
    def post(self, request):
        serializer = OsonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Xabar': "User Registratsiyadan o`tdi"}, status=200)
        else:
            return Response(serializer.errors, status=400)


class LoginAPI(APIView):
    serializer_class = QiynSerializer

    @swagger_auto_schema(request_body=QiynSerializer)
    def post(self, request):
        phone_front = request.data.get('phone')
        password_front = request.data.get('password')

        filtr = PaymeUser.objects.all().filter(phone=phone_front, password=password_front)
        if filtr:
            serializer = OsonSerializer(filtr, many=True)
            return Response(serializer.data, status=200)
        else:
            return Response({'Xabar': 'Bunday Foydalanuvchi Bizda Mavjud emas'}, status=400)


class AddCardAPI(APIView):
    serializer_class = KartaSerializer

    @swagger_auto_schema(request_body=KartaSerializer)
    def post(self, request):
        serializer = KartaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Xabar': "karta qo`shildi"}, status=200)
        else:
            return Response(serializer.errors, status=400)


# 7
class AllCardAPI(APIView):
    def get(self, request):
        print(request)
        hamma_kartalar = BaseCard.objects.all()
        serializer = KartaSerializer(hamma_kartalar, many=True)
        return Response(serializer.data, status=200)


class AllHistoryPayment(APIView):
    def get(self, request):
        print(request)
        hamma_istoriya = PaymentHistory.objects.all()
        serializer = HistorySerializer(hamma_istoriya, many=True)
        return Response(serializer.data, status=200)


class SearchCardAPI(APIView):
    serializer_class = SearchSerializer

    @swagger_auto_schema(request_body=SearchSerializer)
    def post(self, request):
        card_number_front = request.data.get('number')
        # print(card_number_front)
        filtr_karata = BaseCard.objects.all().filter(number=card_number_front)
        serializer = KartaSerializer(filtr_karata, many=True)
        return Response(serializer.data, status=200)

        # card_filtr = BaseCard.objects.all().filter(number=card_number_front)
        # serializer = SearchSerializer(card_filtr,many=True)
        return Response({'Xabar': "Ishlayaptiku"}, status=200)


class DeleteCard(APIView):
    @swagger_auto_schema(request_body=DeleteCardSerializer)
    def delete(self, request):
        karta_raqami = request.data.get('card_number')
        try:
             BaseCard.objects.all().filter(number=karta_raqami).delete()
             return Response({'Xabar': 'Karta o`chirildi'}, status=200)
        except:
            return Response({'Xabar': 'Bunday karta topilmadi'}, status=404)

class DeleteUser(APIView):
    @swagger_auto_schema(request_body=DeletePaymeuserSerializer)
    def delete(self, request):
        phone_number = request.data.get('phone_number')
        try:
            if PaymeUser.objects.all().filter(phone=phone_number).exists():
                PaymeUser.objects.all().filter(phone=phone_number).delete()
                return Response({'Xabar': 'User o`chirildi'}, status=200)
            else:
                return Response({'Xabar': 'Bunday user mavjud emas'}, status=404)

        except:
            return Response({'Xabar': 'Bunday user mavjud emas'}, status=404)
