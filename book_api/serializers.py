from auth_api.models import User
from django.db import models
from django.db.models import Q # for queries
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Book
from django.core.exceptions import ValidationError


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email']

class BookSerializer(serializers.ModelSerializer):
    # ********************
    publisher=PublisherSerializer(many=True)
    # serieslabels = SeriesLabelSerializer(many=True)
    # datalabels = DataLabelSerializer(many=True)

    # class Meta:
    #     model = Chart
    #     fields = ('csv', 'vertical_label', 'horizontal_label', 'serieslabels', 'datalabels')

    class Meta:
        model = Book
        fields = ['title','slug','image','price','publication_date','publisher']

# title = models.CharField(max_length=30)
#     slug = models.SlugField(unique=True)
#     image=models.FileField(default="")
#     # image = models.ImageField(upload_to='uploads/')
#     price=models.IntegerField()
#     publication_date = models.DateTimeField(auto_now_add=True)
   
#     publisher = models.ManyToManyField(User)
    
