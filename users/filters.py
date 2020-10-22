# Django main imports
from django.db import models
# Django Filters imports
from django_filters import rest_framework as filters
from django_filters import IsoDateTimeFilter
# My imports
from .models import Photo, Profile


class PhotoFilter(filters.FilterSet):
    class Meta:
        model = Photo
        fields = ['date', 'meal', 'profile']
        filter_overrides = {
            models.DateTimeField: {
                'filter_class': IsoDateTimeFilter
            },
        }

