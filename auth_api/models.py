from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from passlib.hash import pbkdf2_sha256


class User(AbstractBaseUser, PermissionsMixin):
    name=models.CharField(max_length=50,null=True,blank=False,default="")
    username=models.CharField(max_length=50,null=False,blank=False,unique=True)
    email = models.EmailField(max_length=50,blank=True)
    password = models.CharField(max_length=50)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    ifLogged = models.BooleanField(default=False)
    token = models.CharField(max_length=500, null=True, default="")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = CustomUserManager()

    def __str__(self):
        return "{} -{}".format(self.username, self.email)

    


class User1(models.Model):
    name=models.CharField(max_length=50,null=True,blank=False,default="")
    username=models.CharField(max_length=50,null=False,blank=False,unique=True)
    email = models.EmailField(max_length=50,blank=True)
    password = models.CharField(max_length=50)
    
    token = models.CharField(max_length=500, null=True,blank=True, default="")
    superuser_status=models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    ifLogged = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def verify_password(self, raw_password):
        return pbkdf2_sha256.verify(raw_password,self.password)

    def __str__(self):
        return self.username
        
    


