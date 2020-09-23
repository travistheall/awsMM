# Django main imports
from django.db import models
# Django Filters imports
from django_filters import rest_framework as filters
from django_filters import CharFilter
# My imports
from .models import (Mainfooddesc,
                     Addfooddesc,
                     Foodweights,
                     Fnddsnutval,
                     Nutdesc)


class MainfooddescFilter(filters.FilterSet):
    class Meta:
        model = Mainfooddesc
        fields = ['foodcode', 'mainfooddescription', 'additionalDescriptions__additionalfooddescription']
        filter_overrides = {
            models.CharField: {
                'filter_class': CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            }
        }


class AddfooddescFilter(filters.FilterSet):
    class Meta:
        model = Addfooddesc
        fields = ['foodcode', 'seqnum', 'additionalfooddescription']
        filter_overrides = {
            models.CharField: {
                'filter_class': CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            }
        }


class FoodweightsFilter(filters.FilterSet):
    class Meta:
        model = Foodweights
        fields = ['foodcode']


class FnddsnutvalFilter(filters.FilterSet):
    class Meta:
        model = Fnddsnutval
        fields = ['foodcode']


class NutdescFilter(filters.FilterSet):
    class Meta:
        model = Nutdesc
        fields = ['nutrientcode']
