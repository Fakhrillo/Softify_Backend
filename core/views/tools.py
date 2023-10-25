from rest_framework import generics

from ..models import *
from ..serializers import *

class ToolsListAPIView(generics.ListAPIView):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer