from django.db import models
from django.db.models import Q # for queries
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User,User1
from django.core.exceptions import ValidationError
from uuid import uuid4
# from rest_framework import IsActiveListSerializer
# Admin******************************************


class UserSerializer(serializers.ModelSerializer):
    # ********************
    class Meta:
        model = User
        fields = '__all__'


        # *************************
    # email = serializers.EmailField(
    #     required=True,
    #     validators=[UniqueValidator(queryset=User.objects.all())]
    #     )
    # username = serializers.CharField(
    #     required=True,
    #     validators=[UniqueValidator(queryset=User.objects.all())]
    #     )
    # password = serializers.CharField(max_length=8)

    # class Meta:
    #     model = User
    #     fields = (
    #         'username',
    #         'email',
    #         'password'
        # )


class UserLoginSerializer(serializers.ModelSerializer):
    # to accept either username or email
    user_id = serializers.CharField()
    password = serializers.CharField()
    token = serializers.CharField(required=False, read_only=True)

    def validate(self, data):
        # print("366666666666666666666666666666666666")
        # print(data)
        # user,email,password validator
        user_id = data.get("user_id", None)
        password = data.get("password", None)
        if not user_id and not password:
            raise ValidationError("Details not entered.")
        user = None
        # if the email has been passed
        if '@' in user_id:
            user = User.objects.filter(
                Q(email=user_id) &
                Q(password=password)
                ).distinct()
            if not user.exists():
                raise ValidationError("User credentials are not correct.")
            user = User.objects.get(email=user_id)
        else:
            user = User.objects.filter(
                Q(username=user_id) &
                Q(password=password)
            ).distinct()
            if not user.exists():
                raise ValidationError("User credentials are not correct.")
            user = User.objects.get(username=user_id)
        if user.ifLogged:
            raise ValidationError("User already logged in.")
        user.ifLogged = True
        # print(data)
        # print("helloooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
        data['token'] = uuid4()
        # print(data)
        user.token = data['token']
        user.save()
        return data

    class Meta:
        model = User
        fields = (
            'user_id',
            'password',
            'token',
        )

        read_only_fields = (
            'token',
        )


class UserLogoutSerializer(serializers.ModelSerializer):
    token = serializers.CharField()
    status = serializers.CharField(required=False, read_only=True)

    def validate(self, data):
        token = data.get("token", None)
        print(token)
        user = None
        try:
            user = User.objects.get(token=token)
            if not user.ifLogged:
                raise ValidationError("User is not logged in.")
        except Exception as e:
            raise ValidationError(str(e))
        user.ifLogged = False
        user.token = ""
        user.save()
        data['status'] = "User is logged out."
        return data

    class Meta:
        model = User
        fields = (
            'token',
            'status',
        )


# ***End Admin***********************************************************************************************


# *User1********************************************************************************************************

    # # user_id = serializers.CharField()
    # name=serializers.CharField()
    # username=serializers.CharField()
    # email = serializers.EmailField()
    # password = serializers.CharField()
    # ifLogged = serializers.BooleanField()
    # token = serializers.CharField()
    # is_verified = serializers.BooleanField()
    # is_active = serializers.BooleanField()
    # is_staff = serializers.BooleanField()
    # created_at = serializers.DateTimeField()
    # updated_at = serializers.DateTimeField()
    


    # # *************************************************
    # def validate(self, data):
    #     # print("366666666666666666666666666666666666")
    #     # print(data)
    #     # user,email,password validator
        
    #     is_active = data.get("is_active", None)
    #     user=User.objects.all()
    #     if not is_active.exists():
    #         pass
    #     elif user.is_active:
                        
            
    #         pass
    #     else:
    #         user.save()
        
    #     return data
   
    # # ****************************************************

   

    
class IsActiveListSerializer(serializers.ListSerializer):

            
    def to_representation(self, data):
        data = data.filter(is_active=0)
        return super().to_representation(data)

class UserSerializer1(serializers.ModelSerializer):
    class Meta:
        model = User1
        fields = (
            'name','username','email','password','ifLogged','token','is_verified','is_active','is_staff','created_at','updated_at',)
        list_serializer_class = IsActiveListSerializer

    


class UserLoginSerializer1(serializers.ModelSerializer):
    # to accept either username or email
    user_id = serializers.CharField()
    password = serializers.CharField()
    # status=serializers.CharField()
    token = serializers.CharField(required=False, read_only=True)

    def validate(self, data):
        # print("366666666666666666666666666666666666")
        # print(data)
        # user,email,password validator
        user_id = data.get("user_id", None)
        password = data.get("password", None)
        # status=data.get("status",None)
        if not user_id and not password:
            raise ValidationError("Details not entered.")
        user = None
        # if the email has been passed
        if '@' in user_id:
            user = User1.objects.filter(
                Q(email=user_id) &
                Q(password=password)
                ).distinct()
            if not user.exists():
                raise ValidationError("User credentials are not correct.")
            user = User1.objects.get(email=user_id)


        # if not user.is_active:
        #     raise ValidationError("User should not be login")
       
        else:
            user = User1.objects.filter(
                Q(username=user_id) &
                Q(password=password)
            ).distinct()
            if not user.exists():
                raise ValidationError("User credentials are not correct.")
            user = User1.objects.get(username=user_id)

        if not user.is_active:
            raise ValidationError("User should be active for login")
        print(user)
        if user.ifLogged:
            raise ValidationError("User already logged in.")
        user.ifLogged = True

        # *****************************************************allow permission****************************************
        # if user.is_active:
        #     raise ValidationError("hey admin dashboard profilesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
        # # print(data)
        # print("helloooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
        data['token'] = uuid4()
        # print(data)
        user.token = data['token']
        user.save()
        
        return data

    class Meta:
        model = User1
        fields = (
            'user_id',
            'password',
            'token',
        )

        read_only_fields = (
            'token',
        )


class UserLogoutSerializer1(serializers.ModelSerializer):
    token = serializers.CharField()
    status = serializers.CharField(required=False, read_only=True)

    def validate(self, data):
        token = data.get("token", None)
        print(token)
        user = None
        try:
            user = User1.objects.get(token=token)
            if not user.ifLogged:
                raise ValidationError("User is not logged in.")
        except Exception as e:
            raise ValidationError(str(e))
        user.ifLogged = False
        user.token = ""
        user.save()
        data['status'] = "User is logged out."
        return data

    class Meta:
        model = User1
        fields = (
            'token',
            'status',
        )

# *End User1****************************************************************************************************