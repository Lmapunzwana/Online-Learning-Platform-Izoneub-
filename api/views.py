from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from users.models import Profile
from .serializers import ProfileSerializer

class ProfileListView(APIView, LimitOffsetPagination):
    paginator = LimitOffsetPagination()
    def get(self, request,pk):
        profile = Profile.objects.get(pk=pk)

        # Serialize and return
        results = self.paginate_queryset(profile,request,view=self)
        serializer = ProfileSerializer(results)
        return Response(serializer.data)