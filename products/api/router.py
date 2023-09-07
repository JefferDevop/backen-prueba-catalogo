from rest_framework.routers import DefaultRouter
from products.api.views import GalleryApiViewSet, CategoryApiViewSet, ProductOEApiViewSet, ProductApiViewSet, CategoryProductApiViewSet

router_category = DefaultRouter()
router_product = DefaultRouter()
router_productOE = DefaultRouter()
router_product_category = DefaultRouter()
router_gallery = DefaultRouter()

router_category.register(
    prefix='category', basename='category', viewset=CategoryApiViewSet   
)

router_product.register(
    prefix='products', basename='products', viewset=ProductApiViewSet
)

router_productOE.register(
    prefix='productsOE', basename='productsOE', viewset=ProductOEApiViewSet
)

router_product_category.register(
    prefix='product_category', basename='product_category', viewset=CategoryProductApiViewSet
)

router_gallery.register(
    prefix='gallery', basename='gallery', viewset=GalleryApiViewSet
)