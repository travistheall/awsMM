from django.contrib.auth.models import User, Group
# Django Rest Framework imports
from rest_framework import (permissions,
                            viewsets,
                            status)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import (Profile,
                     Weight,
                     Photo,
                     Food)
from .serializers import (CurrentUserSerializer,
                          UserSerializerWithToken,
                          UserSerializer,
                          GroupSerializer,
                          ProfileSerializer,
                          WeightSerializer,
                          PhotoSerializer,
                          FoodSerializer,)
from .filters import PhotoFilter
from .permissions import IsOwnerOrReadOnly


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    serializer = ProfileSerializer(user=request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
