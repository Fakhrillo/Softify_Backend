from rest_framework import generics
from django.http import Http404

from rest_framework.response import Response

from ..models import *
from ..serializers import *

# Create your views here.
class PortfolioListAPIView(generics.ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    def get_queryset(self):
        category_param = self.request.query_params.get('category', None)

        if category_param == 'all':
            # Return all portfolios
            queryset = Portfolio.objects.all()
        else:
            try:
                # Try to get the Category by its primary key
                category = Category.objects.get(pk=category_param)
                queryset = Portfolio.objects.filter(category=category)
            except Category.DoesNotExist:
                raise Http404("Category does not exist")

        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        portfolio_serializer = self.get_serializer(queryset, many=True)
        
        return Response(portfolio_serializer.data)


class PortfolioRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    def get(self, request, *args, **kwargs):
        types = False
        instance = self.get_object()
        images = PortfolioImages.objects.filter(main_model=instance)
        images_serializer = PortfolioImagesSerializer(images, many=True)
        serializer = self.get_serializer(instance)
        categroy = serializer.data['category_name']
        if categroy.lower() in ['web app', 'app']:
            types = True
        response_data = {
            'portfolio_item': serializer.data,
            'images': images_serializer.data,
            'type': types,
        }
        return Response(response_data)
    
class PortfolioFiveLatest(generics.ListAPIView):
    queryset = Portfolio.objects.order_by('-created_at')[:5]
    serializer_class = PortfolioSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        portfolio_serializer = self.get_serializer(queryset, many=True)
        return Response(portfolio_serializer.data)