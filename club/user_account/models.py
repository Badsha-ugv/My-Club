
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    CLUB_NAME  = (
        ('PROGRAMMING','PROGRAMMING'),
        ('DEVELOPMENT','DEVELOPMENT'),
    )

    GENDER = (
        ('MALE','MALE'),
        ('FEMALE','FEMALE'),
    )

    USER_TYPE =(
        ('ADMIN','ADMIN'),
        ('STAFF','STAFF'),
        ('MEMBERS','MEMBERS'),
        
    )

    email = models.EmailField(max_length=40,blank=True,null=True)
    student_id = models.CharField(max_length=20,unique=True,blank=True,null=True)
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    batch = models.CharField(max_length=20,null=True,blank=True)
    semester = models.CharField(max_length=20,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    gender = models.CharField(max_length=10,null=True,blank=True, choices=GENDER )
    user_type = models.CharField(
        max_length=10, choices=USER_TYPE, blank=True, default='MEMBERS')
    club_name = models.CharField(max_length=15, blank=True,null=True, choices = CLUB_NAME) 
    profile_pic = models.ImageField(upload_to='user_profile/',null=True, blank=True, ) 
    created_at = models.DateField(auto_now_add=True,null=True,blank=True)
    

    def __str__(self):
        return self.username 