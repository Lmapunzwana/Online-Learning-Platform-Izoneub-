from django.db import models
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
import datetime


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Video(models.Model):
    course = models.ForeignKey(Course, related_name='videos', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    resolution = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)  # Comma-separated list of tags
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.thumbnail:
            self.generate_thumbnail()

    def generate_thumbnail(self):
        if self.video_file:
            from moviepy.editor import VideoFileClip
            from PIL import Image

            # Generate a temporary file path for the thumbnail
            temp_thumb_path = f'thumbnails/{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.png'

            # Load video file using moviepy
            clip = VideoFileClip(self.video_file.path)
            # Extract frame at 1 second
            frame = clip.get_frame(1)
            # Convert frame to image and save it as thumbnail
            img = Image.fromarray(frame)
            thumb_io = ContentFile(b'')
            img.save(thumb_io, format='PNG')
            self.thumbnail.save(temp_thumb_path, thumb_io)
            clip.close()


class Comment(models.Model):
    video = models.ForeignKey(Video, related_name='comments', on_delete=models.CASCADE)
    user = models.CharField(max_length=255)  # Simplified for now, can be linked to User model later
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user} on {self.video.title}'


class Rating(models.Model):
    video = models.ForeignKey(Video, related_name='ratings', on_delete=models.CASCADE)
    user = models.CharField(max_length=255)  # Simplified for now, can be linked to User model later
    rating = models.IntegerField()  # Assume rating is an integer between 1 and 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Rating by {self.user} on {self.video.title}'