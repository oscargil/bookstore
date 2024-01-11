from inventory.views import BookViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
urlpatterns = router.urls