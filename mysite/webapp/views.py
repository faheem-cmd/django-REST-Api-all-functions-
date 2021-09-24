import status as status
from Demos.FileSecurityTest import permissions
from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from .models import news
from .models import workers
from .serializers import newsSerializer
from .serializers import workersSerializer
from .serializers import CartItemSerializer
from .models import CartItem
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import permissions
from .serializers import CarsSerializer
from rest_framework.throttling import UserRateThrottle
from .models import Cars


class newsList(APIView):
    def get(self, request):
        news1 = news.objects.all()
        serializer = newsSerializer(news1, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self):
        pass


class workersList(APIView):
    def get(self, request):
        workers1 = workers.objects.all()
        serializer = workersSerializer(workers1, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self):
        pass


class CartItemViews(APIView):
    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


#
# class CartItemViews(APIView):
#
#     def get(self, request, id=None):
#         if id:
#             item = CartItem.objects.get(id=id)
#             serializer = CartItemSerializer(item)
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#
#         items = CartItem.objects.all()
#         serializer = CartItemSerializer(items, many=True)
#         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "status": 200,
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
        })


class LoginAPI(KnoxLoginView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


    # car


class CarsAPIView(APIView):
    serializer_class = CarsSerializer
    throttle_scope = "cars_app"

    def get_queryset(self):
        cars = Cars.objects.all()
        return cars

    def get(self, request, *args, **kwargs):

        try:
            id = request.query_params["id"]
            if id != None:
                car = Cars.objects.get(id=id)
                serializer = CarsSerializer(car)
        except:
            cars = self.get_queryset()
            serializer = CarsSerializer(cars, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        car_data = request.data

        new_car = Cars.objects.create(car_brand=car_data["car_brand"], car_model=car_data[
            "car_model"], production_year=car_data["production_year"], car_body=car_data["car_body"],
                                      engine_type=car_data["engine_type"])

        new_car.save()

        serializer = CarsSerializer(new_car)

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        id = request.query_params["id"]
        car_object = Cars.objects.get(id=id)

        data = request.data

        car_object.car_brand = data["car_brand"]
        car_object.car_model = data["car_model"]
        car_object.production_year = data["production_year"]
        car_object.car_body = data["car_body"]
        car_object.engine_type = data["engine_type"]

        car_object.save()

        serializer = CarsSerializer(car_object)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        car_object = Cars.objects.get()
        data = request.data

        car_object.car_brand = data.get("car_brand", car_object.car_brand)
        car_object.car_model = data.get("car_model", car_object.car_model)
        car_object.production_year = data.get("production_year", car_object.production_year)
        car_object.car_body = data.get("car_body", car_object.car_body)
        car_object.engine_type = data.get("engine_type", car_object.engine_type)

        car_object.save()
        serializer = CarsSerializer(car_object)

        return Response(serializer.data)
