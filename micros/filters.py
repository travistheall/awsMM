# Django main imports
from django.db import models
# Django Filters imports
from django_filters import rest_framework as filters
from django_filters import CharFilter
# My imports
from .models import Mainfooddesc


class FoodSearchFilter(filters.FilterSet):
    class Meta:
        model = Mainfooddesc
        fields = ['foodcode',
                  'mainfooddescription',
                  'additionalDescriptions__additionalfooddescription']
        filter_overrides = {
            models.CharField: {
                'filter_class': CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            }
        }
