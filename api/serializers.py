from rest_framework import serializers
from .models import Course, Video, Comment, Rating

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
            'id', 'course', 'title', 'video_file', 'thumbnail', 'duration',
            'resolution', 'description', 'tags', 'uploaded_at'
        ]

class CourseSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'videos']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'video', 'user', 'text', 'created_at']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'video', 'user', 'rating', 'created_at']