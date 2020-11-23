# Django main imports
from django.db.models import Q
# Django Rest Framework imports
from rest_framework import viewsets
# My imports
from .models import (Mainfooddesc,
                     Fnddsnutval)
from micros.serializers import (FoodSearchSerializers,
                                FnddsnutvalSerializer,
                                MainfooddescSerializer)
from .filters import FoodSearchFilter
from .pagination import NutValSetPagination
from rest_framework.permissions import AllowAny


class FoodSearchView(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Main/Additional
    Food Descriptions from FNDDS to be searched.
    """
    queryset = Mainfooddesc.objects.all().prefetch_related('additionalDescriptions')
    serializer_class = FoodSearchSerializers
    filterset_class = FoodSearchFilter
    permission_classes = [AllowAny]


class MainfooddescSearchView(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Main Food Descriptions from FNDDS to be searched.
    """
    queryset = Mainfooddesc.objects.all()
    serializer_class = MainfooddescSerializer


class PortionNutValSearchView(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Additional Food Descriptions from FNDDS to be searched.
    """
    queryset = Fnddsnutval.objects.filter(
        Q(nutrientcode=208) | Q(nutrientcode=203) | Q(nutrientcode=204) | Q(nutrientcode=205))
    serializer_class = FnddsnutvalSerializer
    pagination_class = NutValSetPagination
