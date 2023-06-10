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
        fields = ['id', 'name', 'position', 'image']


class SlideSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['position', 'image']


class ProductSerializer(ModelSerializer):
    options = SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'offer_price', 'delivery_charge', 'cod', 'star_5', 'star_4', 'star_3', 'star_2', 'star_1', 'options']

    def get_options(self, obj):
        options = obj.options_set.all()
        data = ProductOptionSerializer(options, many=True).data
        return data


class ProductOptionSerializer(ModelSerializer):
    images = SerializerMethodField()
    class Meta:
        model = ProductOption
        fields = ['id', 'option', 'quantity', 'images']

    def get_images(self, obj):
        images = obj.images_set.all()
        data = ProductImageSerializer(images, many=True).data
        return data


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