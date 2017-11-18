from rest_framework.serializers import ModelSerializer

from example.core.models import (
    User,
)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'date_joined')
