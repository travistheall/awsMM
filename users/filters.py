# Django Filters imports
from django_filters import rest_framework as filters
# My imports
from .models import Meal, Profile


class MealFilter(filters.FilterSet):
    class Meta:
        model = Meal
        fields = ['date', 'name', 'profile']
