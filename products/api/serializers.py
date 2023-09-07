from rest_framework.serializers import ModelSerializer
from products.models import Gallery, Category, Product, CategoryProduct, Attribut


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image']



class AttributSerializer(ModelSerializer):
    class Meta:
        model = Attribut
        fields = ['id', 'name']



class ProductSerializer(ModelSerializer):
   # data = CategoryProductSerializer(source='product_id', read_only=True, many=True)
    class Meta:
        model = Product
        fields = ['codigo', 'ref', 'flag', 'name_extend', 'slug', 'description', 'images',
                  'price_old',  'price1', 'price2', 'active', 'soldout', 'offer', 'home']


class GallerySerializer(ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'product', 'image']


class CategoryProductSerializer(ModelSerializer):
    categoryData = CategorySerializer(source='category', read_only=True)
    productData = ProductSerializer(source='product', read_only=True)

    class Meta:
        model = CategoryProduct
        fields = ['id', 'active', 'productData', 'categoryData']
