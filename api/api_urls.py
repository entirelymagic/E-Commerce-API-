from rest_framework import routers

from api.category.views import CategoryViewSet
from api.user.views import UserViewSet
from api.product.views import ProductViewSet


router = routers.DefaultRouter()

router.register(r'category', CategoryViewSet, basename="category")
# registration
router.register(r'user', UserViewSet, basename="user")
router.register(r'product', ProductViewSet, basename="product")