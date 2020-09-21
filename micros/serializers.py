from abc import ABC

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import (Mainfooddesc,
                     Addfooddesc,
                     Foodweights,
                     Foodportiondesc,
                     Fnddsnutval,
                     Nutdesc)
from django.db.models import Q


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


class AddfooddescSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addfooddesc
        fields = [
            'additionalfooddescription'
        ]


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


class FoodweightsSerializer(serializers.ModelSerializer):
    nutval = FnddsnutvalSerializer(many=True, read_only=True)

    class Meta:
        model = Foodweights
        fields = [
            'foodcode',
            'subcode',
            'seqnum',
            'portioncode',
            'portionweight',
            'nutval'
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        portionObj = FoodportiondescSerializer(instance.portioncode).data
        response['portioncode'] = portionObj
        return response


class MainfooddescSerializer(serializers.ModelSerializer):
    additionalDescriptions = AddfooddescSerializer(many=True, read_only=True)
    foodweights = FoodweightsSerializer(many=True, read_only=True)
    nutrientvalues = FnddsnutvalSerializer(many=True, read_only=True, source='abbNutVal')

    class Meta:
        model = Mainfooddesc
        fields = [
            'foodcode',
            'mainfooddescription',
            'additionalDescriptions',
            'foodweights',
            'nutrientvalues',
        ]


class FoodportiondescSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Foodportiondesc
        fields = [
            'portiondescription',
        ]
