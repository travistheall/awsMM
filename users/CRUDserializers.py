from rest_framework import serializers
from .models import Food


class CRUDFoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = [
            'meal',
            'food',
            'servingSize',
            'taken_serving',
            'returned_serving'
        ]
