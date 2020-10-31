# Django main imports
from django.db.models import Q
# Django Rest Framework imports
from rest_framework import viewsets
# My imports
from .models import (Mainfooddesc,
                     Addfooddesc,
                     Foodweights,
                     Foodportiondesc,
                     Fnddsnutval,
                     Nutdesc)
from micros.serializers import (MainfooddescSerializer,
                                AddfooddescSerializer,
                                FoodweightsSerializer,
                                FoodportiondescSerializer,
                                FnddsnutvalSerializer,
                                NutdescSerializer)
from .filters import (MainfooddescFilter,
                      AddfooddescFilter,
                      FoodweightsFilter,
                      FnddsnutvalFilter,
                      NutdescFilter)
from .pagination import (FoodWeightsSetPagination,
                         NutValSetPagination)


class MainfooddescSearchView(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Main Food Descriptions from FNDDS to be searched.
    """
    queryset = Mainfooddesc.objects.all()
    serializer_class = MainfooddescSerializer
    filterset_class = MainfooddescFilter


class AddfooddescSearchView(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Additional Food Descriptions from FNDDS to be searched.
    """
    queryset = Addfooddesc.objects.all()
    serializer_class = AddfooddescSerializer
    filterset_class = AddfooddescFilter


class FoodweightsSearchView(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Additional Food Descriptions from FNDDS to be searched.
    """
    queryset = Foodweights.objects.all()
    serializer_class = FoodweightsSerializer
    filterset_class = FoodweightsFilter
    pagination_class = FoodWeightsSetPagination


class FoodportiondescSearchView(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Additional Food Descriptions from FNDDS to be searched.
    """
    queryset = Foodportiondesc.objects.all()
    serializer_class = FoodportiondescSerializer


class FnddsnutvalAbbrevSearchView(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Additional Food Descriptions from FNDDS to be searched.
    """
    queryset = Fnddsnutval.objects.filter(
        Q(nutrientcode=208) | Q(nutrientcode=203) | Q(nutrientcode=204) | Q(nutrientcode=205))
    serializer_class = FnddsnutvalSerializer
    filterset_class = FnddsnutvalFilter
    pagination_class = NutValSetPagination


class NutdescSearchView(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Additional Food Descriptions from FNDDS to be searched.
    """
    queryset = Nutdesc.objects.all()
    serializer_class = NutdescSerializer
    filterset_class = NutdescFilter
