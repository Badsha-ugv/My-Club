
from django.db import models
from user_account.models import CustomUser 
# Create your models here.
#guest user app 
from guest.models import Image 


# class Member(models.Model):
#     name = models.CharField(max_length=100)
#     student_id = models.CharField(max_length=100,unique=True,)
#     email = models.EmailField(max_length=100,blank=True)
#     phone = models.CharField(max_length=100,blank=True)
#     address = models.CharField(max_length=200,blank=True)
#     batch = models.CharField(max_length=50,blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.name




class Payment(models.Model):
    member = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    pay_amount = models.IntegerField()
    due_amount = models.IntegerField(default=0,null=True)
    pay_date = models.DateField()
    
    def __str__(self):
        return "Pay " + str(self.pay_amount) + " Due " + str(self.due_amount) + " " + str(self.member.username)


class Due(models.Model):
    member = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='member')
    ammount = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return "Due " + str(self.ammount) + " " + str(self.member.username)


class Fund(models.Model):
    total = models.IntegerField(default=0)

    def __str__(self):
        return str(self.total)



class Expense(models.Model):
    expense_amount = models.IntegerField() 
    description = models.TextField() 
    date = models.DateField() 
    def __str__(self):
        return str(self.expense_amount) +' '+ str(self.date) 
         
class Event(models.Model):
    STATUS = (
        ('COMPLETE','COMPLETE'),
        ('UPCOMMING','UPCOMMING'),  
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    event_status = models.CharField(max_length=20, default='UPCOMMING', choices=STATUS, null=True, blank=True)
    
    def __str__(self):
        return str(self.name)
        


# Guest User Management
