from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import (Mainfooddesc,
                     Addfooddesc,
                     Foodweights,
                     Foodportiondesc,
                     Fnddsnutval,
                     Nutdesc)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url',
            'username',
            'email',
            'groups'
        ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class MainfooddescSerializer(serializers.ModelSerializer):
    additionalDescriptions = serializers.StringRelatedField(many=True)
    foodcode_ingredients = serializers.StringRelatedField(many=True)

    class Meta:
        model = Mainfooddesc
        fields = [
            'foodcode',
            'mainfooddescription',
            'additionalDescriptions',
            'foodcode_ingredients'
        ]


class AddfooddescSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addfooddesc
        fields = [
            'foodcode',
            'seqnum',
            'additionalfooddescription'
        ]


class FoodportiondescSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Foodportiondesc
        fields = [
            'portiondescription',
        ]


class FoodweightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foodweights
        fields = [
            'foodcode',
            'subcode',
            'seqnum',
            'portioncode',
            'portionweight',
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        portionObj = FoodportiondescSerializer(instance.portioncode).data
        response['portioncode'] = portionObj
        return response


class NutdescSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nutdesc
        fields = [
            'nutrientdescription',
        ]


class FnddsnutvalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fnddsnutval
        fields = [
            'foodcode',
            'nutrientcode',
            'nutrientvalue'
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        nutrObj = NutdescSerializer(instance.nutrientcode).data
        response['nutrientcode'] = nutrObj
        return response
