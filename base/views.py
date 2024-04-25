from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
# Create your views here.

class ResourceTypeView(ModelViewSet):
    queryset = ResourceType.objects.all()
    serializer_class = ResourceTypeSerializer


class ResourceView(GenericAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

    def get(self,request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


    






class DepartmentView(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

# class ResourceView(ModelViewSet):
#     queryset = Resource.objects.all()
#     serializer_class = ResourceSerializer

class VendorView(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseView(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
