
from django.db import models
from user_account.models import CustomUser



class DevPayment(models.Model):
    member = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pay_amount = models.IntegerField()
    due_amount = models.IntegerField(default=0, null=True)
    pay_date = models.DateField()

    def __str__(self):
        return "Pay " + str(self.pay_amount) + " Due " + str(self.due_amount) + " " + str(self.member.name)


class DevDue(models.Model):
    member = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    ammount = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True   )

    def __str__(self):
        return "Due " + str(self.ammount) + " " + str(self.member.name)


class DevFund(models.Model):
    total = models.IntegerField(default=0)

    def __str__(self):
        return str(self.total)


class DevExpense(models.Model):
    expense_amount = models.IntegerField()
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return str(self.expense_amount) + ' ' + str(self.date)


class DevEvent(models.Model):
    STATUS = (
        ('COMPLETE', 'COMPLETE'),
        ('UPCOMMING', 'UPCOMMING'),
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    event_status = models.CharField(
        max_length=20, default='UPCOMMING', choices=STATUS, null=True, blank=True)

    def __str__(self):
        return str(self.name)
