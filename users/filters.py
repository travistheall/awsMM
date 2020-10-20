# Django Filters imports
from django_filters import rest_framework as filters
# My imports
from .models import Photo, Profile


class PhotoFilter(filters.FilterSet):
    class Meta:
        model = Photo
        fields = ['created_at', 'meal', 'profile']


