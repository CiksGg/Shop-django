from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet ,RatingViewSet

router = DefaultRouter()
router.register('comments', CommentViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = [
    path('',include(router.urls)),
]