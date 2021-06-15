from rest_framework.serializers import HyperlinkedModelSerializer
from django.contrib.auth.models import User, Group


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'email']
        extra_kwargs = {'password': {'write_only': True}}
        depth = 1
