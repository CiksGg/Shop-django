from rest_framework.serializers import ModelSerializer
from .models import Category, Product

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance: Product):
        rep = super().to_representation(instance)
        rep['category'] = CategorySerializer(instance.category).data
        return rep