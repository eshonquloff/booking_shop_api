from django.urls import path, include
from rest_framework.routers import DefaultRouter

from book.views import BookModelViewSet

router = DefaultRouter()
router.register('books', BookModelViewSet, basename='books')

urlpatterns = [
    path('', include(router.urls))
]
