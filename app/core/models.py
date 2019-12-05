# Django Application Imports
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    ''' to manage user creation nd superuser creation'''
    def create_user(self, first_name,last_name,username,email,password, **kwargs):
        ''' Create and Save new user'''
        user = self.model(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, first_name,last_name,username,email,password):
        ''' create superuser class with same inputs as create user class '''
        user = self.create_user(first_name=first_name,
                                last_name=last_name,
                                username=username,
                                email=email,
                                password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
    
class User(AbstractBaseUser,PermissionsMixin):
    ''' ORM model for user table'''

    username = models.CharField(max_length=255,null=False,unique=True)
    email = models.EmailField(max_length=255,unique=True,null=False)
    first_name = models.CharField(max_length=255,null=False)
    last_name = models.CharField(max_length=255,null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def full_name(self):
        ''' returns the full name of the user

        :return: full_name
        '''

        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        ''' returns the string representation of the object
        
        :return: full_name
        '''
        return self.full_name()

