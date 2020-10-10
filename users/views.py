from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# Django Rest Framework imports
from rest_framework import (permissions,
                            viewsets,
                            status,
                            generics,
                            mixins)
from rest_framework.response import Response
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import (Profile,
                     Weight,
                     Photo,
                     Food)
from .serializers import (UserSerializer,
                          GroupSerializer,
                          ProfileSerializer,
                          WeightSerializer,
                          PhotoSerializer,
                          FoodSerializer,
                          CustomUserSerializer,
                          MyTokenObtainPairSerializer,)
from .filters import (WeightFilter,
                      PhotoFilter)
from .permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

class ObtainTokenPair(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAdminUser,)


class ProfileSearchView(viewsets.ModelViewSet):
    """
    API endpoint that allows Profiles to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class WeightSearchView(viewsets.ModelViewSet):
    """
    API endpoint that allows user weights to be viewed or edited.
    """
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer
    filterset_class = WeightFilter
    permission_classes = (
        IsOwnerOrReadOnly,)


class PhotoSearchView(viewsets.ModelViewSet):
    """
    API endpoint that allows user photos to be viewed or edited.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    filterset_class = PhotoFilter
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,)


class FoodSearchView(viewsets.ModelViewSet):
    """
    API endpoint that allows user foods to be viewed or edited.
    """
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
