from rest_framework import serializers
from django.contrib.auth.models import User
# from rest_framework import employees
from .models import news
from .models import workers
from .models import CartItem
from .models import Cars

#add data
class newsSerializer(serializers.ModelSerializer):
    class Meta:
        model = news
        fields = '__all__'


class workersSerializer(serializers.ModelSerializer):
    class Meta:
        model = workers
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    age = serializers.IntegerField()
    quantity = serializers.IntegerField()
    address = serializers.CharField(max_length=200)

    class Meta:
        model = CartItem
        fields = '__all__'


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ['id', 'car_brand', 'car_model',
                  'production_year', 'car_body', 'engine_type']
