from rest_framework.serializers import ModelSerializer
from core.pos.models import Category, Product


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "image", "slug", "image_alterna"]


class ProductSerializer(ModelSerializer):
    # atributData = AttributSerializer(source='atribut', read_only=True, many=True)
    class Meta:
        model = Product
        fields = [
            "id",
            "code",
            "ref",
            "flag",
            "name",
            "slug",
            "description",          
            "category",
            "image",        
            "image_alterna",
            "pvp",
            "price",
            "stock",      
            "active",
            "soldout",
            "offer",
            "home",       
        ]
