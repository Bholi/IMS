from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
# Create your views here.

class ResourceTypeView(ModelViewSet):
    queryset = ResourceType.objects.all()
    serializer_class = ResourceTypeSerializer

class DepartmentView(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class ResourceView(ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

class VendorView(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseView(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
