from rest_framework import viewsets, permissions
from .models import Course, Video, Comment, Rating
from .serializers import CourseSerializer, VideoSerializer, CommentSerializer, RatingSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('query', '')
        videos = Video.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(tags__icontains=query)
        )
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def recommend(self, request, pk=None):
        video = self.get_object()
        tags = video.tags.split(',') if video.tags else []
        recommended_videos = Video.objects.filter(
            ~Q(id=video.id),
            Q(tags__in=tags) | Q(course=video.course)
        ).distinct()[:5]  # Limit to 5 recommendations
        serializer = VideoSerializer(recommended_videos, many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]