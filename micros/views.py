# Django main imports
from django.shortcuts import render
from django.contrib.auth.models import User, Group
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
from .serializers import (UserSerializer,
                          GroupSerializer,
                          MainfooddescSerializer,
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


def home(request):
    context = {'home': 'home',
               'foods': Mainfooddesc.objects.filter(mainfooddescription__icontains='milk')}
    return render(request, 'micros/home.html', context)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


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
