from rest_framework import generics

from ..models import *
from ..serializers import *

class TeamListAPIView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer