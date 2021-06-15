from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView

from .serializers import UserSerializer


class UserViewSet(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
