from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, VideoViewSet, CommentViewSet, RatingViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]