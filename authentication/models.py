from django.db import models
from django.contrib.auth.models import AbstractUser

# manager to dictate how to create super user and normal users
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _ # help us raise value error

from phonenumber_field.modelfields import PhoneNumberField 

# Create your models here.

# create custom user model

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Email should be provided"))
        
        # normalizing email
        email = self.normalize_email(email)

        new_user = self.model(email=email, **extra_fields)

        new_user.setpassword(password)

        new_user.save()

        return new_user
    

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Super user should have is_staff to True"))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Super user should have is_superuser to True"))

        if extra_fields.get('is_active') is not True:
            raise ValueError(_("Super user should have is_active to True"))


        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=80, unique=True)
    phone_number = PhoneNumberField(null=False, unique=True)

    USERNAME_FIELD='email'

    REQUIRED_FIELDS=['username', 'phone_number']

    def __str__(self):
        return f"<User {self.email}"