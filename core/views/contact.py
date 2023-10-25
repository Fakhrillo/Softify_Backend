from rest_framework import generics

from ..models import *
from ..serializers import *

class ContactListAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer