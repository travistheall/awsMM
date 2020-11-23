from rest_framework import serializers
from micros.models import (Mainfooddesc,
                           Addfooddesc,
                           Foodweights,
                           Foodportiondesc,
                           Fnddsnutval,
                           Nutdesc)


# 1 cup, 1 slice of pizza, etc
class FoodportiondescSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foodportiondesc
        fields = ['portiondescription']


# Brands other names, etc
class AddfooddescSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addfooddesc
        fields = ['additionalfooddescription']


# Protein, Carbs, Fat, etc
class NutdescSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutdesc
        fields = ['nutrientdescription']


class FnddsnutvalSerializer(serializers.ModelSerializer):
    nutrientdescription = NutdescSerializer(many=False, read_only=True)

    class Meta:
        model = Fnddsnutval
        fields = [
            'nutrientcode',
            'nutrientdescription',
            'nutrientvalue'
        ]

    #def to_representation(self, instance):
        #response = super().to_representation(instance)
        #print(response['nutrientcode'])
        #nutrientObj = NutdescSerializer(nutrientcode=instance.nutrientcode) .data["nutrientdescription"]
        #print(nutrientObj)
        #response['nutrientcode'] = nutrientObj
        #return response


class FoodweightsSerializer(serializers.ModelSerializer):
    nutval = FnddsnutvalSerializer(many=True, read_only=True)

    class Meta:
        model = Foodweights
        fields = [
            'portioncode',
            'portionweight',
            'nutval'
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        portionObj = FoodportiondescSerializer(instance.portioncode).data
        for key, value in portionObj.items():
            response[key] = value
        return response


class FoodSearchSerializers(serializers.ModelSerializer):
    additionalDescriptions = AddfooddescSerializer(many=True, read_only=True)

    class Meta:
        model = Mainfooddesc
        fields = [
            'foodcode',
            'mainfooddescription',
            'additionalDescriptions',
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        #addDescObj = AddfooddescSerializer(instance.additionalDescriptions).data
        print(len(response['additionalDescriptions']))

        #response['portiondescription'] = portionObj
        return response


class MainfooddescSerializer(serializers.ModelSerializer):
    additionalDescriptions = AddfooddescSerializer(many=True, read_only=True)
    foodweights = FoodweightsSerializer(many=True, read_only=True)
    #nutrientvalues = FnddsnutvalSerializer(many=True, read_only=True, source='abbNutVal')

    class Meta:
        model = Mainfooddesc
        fields = [
            'foodcode',
            'mainfooddescription',
            'additionalDescriptions',
            'foodweights',
            #'nutrientvalues',
        ]


class FoodportiondescSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foodportiondesc
        fields = [
            'portiondescription',
        ]


class MealFnddsnutvalSerializer(serializers.ModelSerializer):
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


