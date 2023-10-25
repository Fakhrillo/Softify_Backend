from rest_framework import generics

from ..models import *
from ..serializers import *

class OurClientsListAPIView(generics.ListAPIView):
    queryset = OurClient.objects.all()
    serializer_class = OurClientSerializer