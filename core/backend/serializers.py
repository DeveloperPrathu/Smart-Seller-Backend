from rest_framework.serializers import ModelSerializer

from backend.models import User, Category


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'phone', 'fullname']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'position', 'image']


class SlideSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['position', 'image']