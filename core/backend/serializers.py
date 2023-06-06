from rest_framework.serializers import ModelSerializer

from backend.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'phone', 'fullname']