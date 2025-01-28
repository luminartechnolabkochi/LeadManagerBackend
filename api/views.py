from django.shortcuts import render

# Create your views here.


# lead Create,List,Retrieve,Update,Delete

from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from api.serializers import LeadSerializer
from api.models import Lead
from django.db.models import Q

class LeadListCreateView(CreateAPIView,ListAPIView):

    serializer_class=LeadSerializer

    queryset=Lead.objects.all()

    def get_queryset(self):
        
        #http://127.0.0.1:8000/api/leads/?search_text=bin

        filter_text=self.request.query_params #{"search_text":"bin"}

        qs=Lead.objects.all()

        if filter_text:

            search_value=filter_text.get("search_text")

            qs=qs.filter(Q(name__contains=search_value)|Q(email__contains=search_value))

        return qs

        






    



    


class LeadRetrieveUpdateDestroyView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    serializer_class=LeadSerializer

    queryset=Lead.objects.all()
