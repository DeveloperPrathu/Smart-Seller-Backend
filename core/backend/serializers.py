from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from backend.models import User, Category, Product, ProductOption, ProductImage, PageItem


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


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['__all__']


class ProductOptionSerializer(ModelSerializer):
    class Meta:
        model = ProductOption
        fields = ['__all__']


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['position', 'image', 'product_option']


class PageItemSerializer(ModelSerializer):
    product_options = SerializerMethodField()

    class Meta:
        model = PageItem
        fields = ['id', 'position', 'image', 'category', 'title', 'viewtype', 'product_options']

    def get_product_options(self, obj):
        options = obj.product_options.all()[:8]
        data = []
        for option in options:
            data.append({
                'id': option.product.id,
                'image': ProductImageSerializer(option.images_set.order_by('position').first(), many=False).data.get('image'),
                'title': option.__str__(),
                'price': option.product.price,
                'offer_price': option.product.offer_price
            })

        return data
