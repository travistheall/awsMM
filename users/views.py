from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# Django Rest Framework imports
from rest_framework import (permissions,
                            viewsets,
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
                          RegistrationSerializer)
from .filters import (WeightFilter,
                      PhotoFilter)
from .permissions import IsOwnerOrReadOnly
from rest_framework.authtoken.models import Token


@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            data = {
                "response": "Successfully registers a new user",
                "email": user.email,
                "username": user.username,
                "token": Token.objects.get(user=user).key
            }
        else:
            data = serializer.errors
        return Response(data)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


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
        IsOwnerOrReadOnly, )


class FoodSearchView(viewsets.ModelViewSet):
    """
    API endpoint that allows user foods to be viewed or edited.
    """
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


