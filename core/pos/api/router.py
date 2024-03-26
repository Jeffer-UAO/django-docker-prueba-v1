from rest_framework.routers import DefaultRouter
from .views import CategoryApiViewSet, ProductApiViewSet



router_category = DefaultRouter()
router_category.register(
    prefix='category', basename='category', viewset=CategoryApiViewSet   
)

router_product = DefaultRouter()
router_product.register(
    prefix='products', basename='products', viewset=ProductApiViewSet
)