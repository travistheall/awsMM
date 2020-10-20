from users.serializers import CurrentUserSerializer, ProfileSerializer
from django.contrib.auth.models import User


def my_jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': CurrentUserSerializer(user, context={'request': request}).data
    }
