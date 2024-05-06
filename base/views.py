from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny,DjangoModelPermissions
# Create your views here.

class ResourceTypeView(ModelViewSet):
    queryset = ResourceType.objects.all()
    serializer_class = ResourceTypeSerializer


class ResourceView(GenericAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    filterset_fields = ['type','department']
    search_fields = ['name']

    def get(self,request):
        queryset = self.get_queryset()
        filtered_queryset = self.filter_queryset(queryset)
        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        data = request.data #The Json Data Sent in Request
        serializer = self.serializer_class(data=data) #The Json Data is converted in Objects by the searializer class
        if serializer.is_valid():
            serializer.save() # Save method automatically creates table in database
            return Response(serializer.data)
            # return Response('Data created')
        else:
            return Response(serializer.errors)
        
class ResourceDetailView(GenericAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

    def get(self,request,pk):
        try:
            resource_data = Resource.objects.get(id=pk)
        except:
            return Response('Data not found',status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(resource_data)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            resource_data = Resource.objects.get(id=pk)
        except:
            return Response('Data not found',status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(resource_data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data Updated')
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk):
        try:
            resource_data = Resource.objects.get(id=pk)
        except:
            return Response('Data not found',status=status.HTTP_404_NOT_FOUND)
        resource_data.delete()
        return Response('Data Deleted!')



class DepartmentView(GenericAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get(self,request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class VendorView(GenericAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def get(self,request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    

class PurchaseView(GenericAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    def get(self,request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    # Only post method is used in this functions
    password = request.data.get('password')
    hash_password = make_password(password)
    request.data['password'] = hash_password
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('User Created')
    else:
        return Response(serializer.errors)
    
    # if request.method == 'GET':
    #     pass
    # elif request.method == 'POST':
    #     pass
    # elif request.method == 'PUT':
    #     pass

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(username=email,password=password)
    if user is None:
        return Response('Invalid email or password',status=status.HTTP_400_BAD_REQUEST)
    else:
        token,_ = Token.objects.get_or_create(user=user)
        return Response(token.key)