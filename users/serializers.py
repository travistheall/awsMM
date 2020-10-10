from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import (Profile,
                     Weight,
                     Photo,
                     Food)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        return token


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


# Register serializer
class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'password2', 'email')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        user = User(username=self.validated_data['username'],
                    email=self.validated_data['email'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})

        user.set_password(password)
        user.save()
        return user


class WeightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weight
        fields = [
            'weight',
            'weightUnit',
            'profile',
            'created_at',
            'updated_at'
        ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        WEIGHT_UNIT_CHOICES = {
            2.20462: "Pounds",
            1: "Kilograms"
        }
        unit = WEIGHT_UNIT_CHOICES.get(instance.weightUnit)
        response['weightUnit'] = unit
        return response


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    weights = WeightSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = [
            'user',
            'image',
            'sex',
            'age',
            'weights',
            'height',
            'heightUnit',
            'activityLevel'
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        SEX_CHOICES = {5: "Male", -161: "Female"}
        gender = SEX_CHOICES.get(instance.sex)
        response['sex'] = gender
        HEIGHT_UNIT_CHOICES = {
            2.54: "Inches",
            1: "Centimeters",
        }
        h_unit = HEIGHT_UNIT_CHOICES.get(instance.heightUnit)
        response['heightUnit'] = h_unit
        ACTIVITY_LEVEL_CHOICES = {
            1.2: "Sedentary",
            1.375: "Light Activity",
            1.55: "Moderately Active",
            1.725: "Very Active",
            1.9: "Extremely Active",
        }
        a_level = ACTIVITY_LEVEL_CHOICES.get(instance.activityLevel)
        response['activityLevel'] = a_level
        return response


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = [
            'food',
            'servingSize',
            'taken_serving',
            'returned_serving'
        ]


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    photos_foods = FoodSerializer(many=True, read_only=True)

    class Meta:
        model = Photo
        fields = [
            'id',
            'profile',
            'meal',
            'photos_foods',
            'image',
            'description',
            'created_at',
            'updated_at'
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        MEAL_CHOICES = {
            "b": "Breakfast",
            "ms": "Morning Snack",
            "l": 'Lunch',
            "as": "Afternoon Snack",
            "d": "Dinner",
            "es": "Evening Snack",
            "mns": "Midnight Snack"
        }
        mealName = MEAL_CHOICES.get(instance.meal)
        response['meal'] = mealName
        return response
