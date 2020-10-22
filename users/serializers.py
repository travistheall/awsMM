from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import (Profile,
                     Weight,
                     Photo,
                     Food)


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'id')


class UserSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password', 'email')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class WeightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weight
        fields = "__all__"

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
    weights = WeightSerializer(many=True, read_only=False)
    user = UserSerializer(many=False, read_only=False)

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
            'photo',
            'food',
            'servingSize',
            'taken_serving',
            'returned_serving',
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
            'updated_at',
            'date'
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
