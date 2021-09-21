from django.db import models
from auth_api.models import User
# ,User1

# Create your models here.


# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     slug = models.SlugField(unique=True)
#     image=models.FileField(default="")
#     # image = models.ImageField(upload_to='uploads/')
#     price=models.IntegerField()
   
#     publisher = models.ForeignKey(User,on_delete=models.CASCADE)
#     publication_date = models.DateTimeField(auto_now_add=True)


    
#     def __str__(self):
#         return self.title
        
#     class Meta:
#         db_table = "Book"




class Book(models.Model):
    # pass
   
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    image=models.FileField(default="")
    # image = models.ImageField(upload_to='uploads/')
    price=models.IntegerField()
    publication_date = models.DateTimeField(auto_now_add=True)
   
    publisher = models.ManyToManyField(User)
    


    
    def __str__(self):
        return self.title
        
    class Meta:
        db_table = "Book"
