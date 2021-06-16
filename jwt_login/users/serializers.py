from rest_framework.serializers import Serializer, CharField, ReadOnlyField, ValidationError, ModelSerializer
from django.contrib.auth.forms import UserCreationForm
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'email']
        extra_kwargs = {'password': {'write_only': True}}
        depth = 1


class RegisterSerializer(Serializer):
    username = CharField(max_length=150)
    password2 = CharField(max_length=150)
    refresh = ReadOnlyField()
    token = ReadOnlyField()

    def validate(self, data):
        data['password1'] = data['password2']
        form = UserCreationForm(data)
        if not form.is_valid():
            raise ValidationError(form.errors)
        return data

    def create(self, validated_data):
        form = UserCreationForm(validated_data)
        if form.is_valid():
            user = form.save()
            refresh = RefreshToken.for_user(user)
            return {
                'username': validated_data['username'],
                'password2': '********',
                'refresh': str(refresh),
                'token': str(refresh.access_token),
            }
        raise ValidationError(form.errors)
