from rest_framework import serializers
from .models import (Mainfooddesc,
                     Addfooddesc,
                     Foodweights,
                     Foodportiondesc,
                     Fnddsnutval,
                     Nutdesc)


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
            'id',
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


class MealFnddsnutvalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fnddsnutval
        fields = [
            'nutrientcode',
            'nutrientvalue'
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        nutrientObj = NutdescSerializer(instance.nutrientcode).data["nutrientdescription"]
        response['nutrientcode'] = nutrientObj
        return response


class MealMainfooddescSerializer(serializers.ModelSerializer):
    nutrientvalues = MealFnddsnutvalSerializer(many=True, read_only=True, source='abbNutVal')
    foodweight = FoodweightsSerializer(many=False, read_only=True)

    class Meta:
        model = Mainfooddesc
        fields = [
            'foodcode',
            'mainfooddescription',
            'foodweight',
            'nutrientvalues',
        ]


class MealFoodweightsSerializer(serializers.ModelSerializer):
    nutval = FnddsnutvalSerializer(many=True, read_only=True)

    class Meta:
        model = Foodweights
        fields = [
            'nutval',
            'portionweight',
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        portionObj = FoodportiondescSerializer(instance.portioncode).data['portiondescription']
        response['portiondescription'] = portionObj
        return response