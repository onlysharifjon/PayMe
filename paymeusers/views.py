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


class ChangePassword(APIView):
    @swagger_auto_schema(request_body=ChangePasswordSerializer)
    def patch(self, request):
        phone = request.data.get('phone')
        name = request.data.get('name')
        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')
        if confirm_password == new_password:
            user = PaymeUser.objects.all().filter(name=name, phone=phone).update(password=new_password)
            return Response({'parol': "o`zgartirildi"}, status=200)
        else:
            return Response({'xabar': "Parol to`g`ri kiritildmadi"})


class Transaction(APIView):
    @swagger_auto_schema(request_body=Transaction)
    def post(self, request):
        card_sender = request.data.get('card_sender')
        card_getter = request.data.get('card_getter')
        money = request.data.get('money')
        money_commissiya = money + (money * 0.01)
        user_card = BaseCard.objects.all().filter(number=card_sender)

        for i in user_card:
            if i.money >= money_commissiya:
                i.money -= money_commissiya
                user_card.update(money=i.money - money_commissiya)
            else:
                return Response({'msg': "Sizda pul yoq"})

        filter_getter = BaseCard.objects.all().filter(number=card_getter)
        for i in filter_getter:
            filter_getter.update(money=i.money + money)
        bank_name = Bank.objects.all().filter(name="PayMe")
        for i in bank_name:
            bank_name.update(money=i.money + (money * 0.01))
        Transactions.objects.create(sender=card_sender, getter=card_getter, money=money_commissiya)
        return Response({'xabar:': f"Sizdan {money_commissiya} miqdorida pul yechildi"})


class SearchUser(APIView):
    def get(self, request, id):
        a = PaymeUser.objects.all().filter(id=id)
        serializer = OsonSerializer(a, many=True)
        return Response(serializer.data)
        # if serializer.is_valid():
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors)


class SortedMoney(APIView):
    def get(self, request):
        money_sorted = Transactions.objects.all().order_by('-money')
        serializer = HistoryTransactions(money_sorted, many=True)
        return Response(serializer.data)


class SearchByNumber(APIView):
    @swagger_auto_schema(request_body=DeletePaymeuserSerializer)
    def post(self, request):
        try:
            phone = request.data.get('phone_number')
            filter_1 = PaymeUser.objects.all().filter(phone=phone).first()
            filter_2 = BaseCard.objects.all().filter(owner_name_id=filter_1.id)
            serializer = KartaSerializer(filter_2, many=True)
            return Response(serializer.data)
        except:
            return Response({'msg': "Bunday raqam mavjud emas"})


class TopMonthTransactionUser(APIView):
    def get(self, request):
        new_database = {}
        fake_database = {}
        all_users = Transactions.objects.all()
        for i in all_users:
            fake_database[i.sender] = 0
        for d in all_users:
            fake_database[d.sender] += d.money
        for i in fake_database.keys():

            user_name = BaseCard.objects.all().filter(number=i)
            for d in user_name:
                print(i, d.owner_name)
                money = fake_database[i]
                new_database[str(d.owner_name)] = money

        sorted_database = dict(sorted(new_database.items(), key=lambda item: item[1],reverse=True))
        return Response(sorted_database)
