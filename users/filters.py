# Django main imports
from django.db import models
# Django Filters imports
from django_filters import rest_framework as filters
from django_filters import CharFilter
# My imports
from .models import (
    Weight,
    Photo,
    Food)


class WeightFilter(filters.FilterSet):
    class Meta:
        model = Weight
        fields = ['created_at']


class PhotoFilter(filters.FilterSet):
    class Meta:
        model = Photo
        fields = ['created_at', 'meal', 'profile']
