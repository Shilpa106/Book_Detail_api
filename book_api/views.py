from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView
from .models import Book
# , User,User1
# from rest_framework import Q
from .serializers import BookSerializer
# , UserLoginSerializer, UserLogoutSerializer,UserSerializer1, UserLoginSerializer1, UserLogoutSerializer1

from rest_framework.filters import OrderingFilter
# from django.contrib.auth.hashers import make_password
# Admin*************************************

class BookRecord(generics.ListCreateAPIView):
    # get method handler
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends=[SearchFilter]
   
    search_fields=['title','price']
    
    
   