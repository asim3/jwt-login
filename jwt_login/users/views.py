from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User

from .serializers import UserSerializer, RegisterSerializer


class UserViewSet(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]  # default
