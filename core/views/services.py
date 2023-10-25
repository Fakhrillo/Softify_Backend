from rest_framework import generics

from rest_framework.response import Response

from ..models import *
from ..serializers import ServiceSerializer

# Create your views here.
class ServiceListAPIView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.serializer_class(queryset, many=True, context={'request':request})

        # Serialize only the 'id', 'icon', 'title', and 'heading' fields
        data = [{'id': item['id'], 'icon': item['icon'], 'title': item['title'], 'heading': item['heading']} for item in serializer.data]
        
        return Response(data)
    

class ServiceRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceCategroyListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.serializer_class(queryset, many=True, context={'request':request})

        # Serialize only the 'id', 'icon', 'title', and 'heading' fields
        data = [{'id': item['id'], 'title': item['title']} for item in serializer.data]
        
        return Response(data)