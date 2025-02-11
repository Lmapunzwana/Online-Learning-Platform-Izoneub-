from django.urls import path
from .views import ProfileListView

urlpatterns = [
    path('profiles/<int:pk>/', ProfileListView.as_view(), name='profile'),
]