# from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import User,User1
# from rest_framework import Q
from .serializers import UserSerializer, UserLoginSerializer, UserLogoutSerializer,UserSerializer1, UserLoginSerializer1, UserLogoutSerializer1

from rest_framework.filters import OrderingFilter

# Admin*************************************

class Record(generics.ListCreateAPIView):
    # get method handler
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Login(generics.GenericAPIView):
    # get method handler
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLoginSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


class Logout(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserLogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLogoutSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


def index(request):
    return redirect('/api/login')





# #End  Admin*************************************

# ***User1***************************************************
class Record1(generics.ListCreateAPIView):
    # get method handler
    queryset = User1.objects.all()
    serializer_class = UserSerializer1

           
    filter_backends = [OrderingFilter]
    ordering_fields = ['created_at']

   
        






class Login1(generics.GenericAPIView):
    # get method handler
    queryset = User1.objects.all()
    serializer_class = UserLoginSerializer1

    def post(self, request, *args, **kwargs):
        serializer_class = UserLoginSerializer1(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


class Logout1(generics.GenericAPIView):
    queryset = User1.objects.all()
    serializer_class = UserLogoutSerializer1

    def post(self, request, *args, **kwargs):
        serializer_class = UserLogoutSerializer1(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


# ***End User1***********************************************