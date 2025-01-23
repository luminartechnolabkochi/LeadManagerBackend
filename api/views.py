from django.shortcuts import render

# Create your views here.


# lead Create,List,Retrieve,Update,Delete

from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from api.serializers import LeadSerializer
from api.models import Lead

class LeadListCreateView(CreateAPIView,ListAPIView):

    serializer_class=LeadSerializer

    queryset=Lead.objects.all()



class LeadRetrieveUpdateDestroyView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    serializer_class=LeadSerializer

    queryset=Lead.objects.all()
