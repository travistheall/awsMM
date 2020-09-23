from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# Django Rest Framework imports
from rest_framework import viewsets
from .models import (Profile,
                     Weight,
                     Photo,
                     Food)
from .serializers import (UserSerializer,
                          GroupSerializer,
                          ProfileSerializer,
                          WeightSerializer,
                          PhotoSerializer,
                          FoodSerializer)
from .filters import (WeightFilter,
                      PhotoFilter)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


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


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


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


class PhotoSearchView(viewsets.ModelViewSet):
    """
    API endpoint that allows user photos to be viewed or edited.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    filterset_class = PhotoFilter


class FoodSearchView(viewsets.ModelViewSet):
    """
    API endpoint that allows user foods to be viewed or edited.
    """
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
