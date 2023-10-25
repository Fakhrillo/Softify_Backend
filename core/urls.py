from django.urls import path
from .views.services import *
from .views.portfolio import *
from .views.tools import *
from .views.ourclients import *
from .views.team import *
from .views.category import *
from .views.contact import *

urlpatterns = [
    path('services/', ServiceListAPIView.as_view()),
    path('services/<int:pk>', ServiceRetrieveAPIView.as_view()),
    path('services/category', ServiceCategroyListView.as_view()),
    
    path('portfolio/', PortfolioListAPIView.as_view()),
    path('portfolio/<int:pk>', PortfolioRetrieveAPIView.as_view()),
    path('portfolio/latest', PortfolioFiveLatest.as_view()),

    path('tools/', ToolsListAPIView.as_view()),
    path('clients/', OurClientsListAPIView.as_view()),
    path('team/', TeamListAPIView.as_view()),
    path('category/', CategoryListAPIView.as_view()),
    path('contact/', ContactListAPIView.as_view()),
]
