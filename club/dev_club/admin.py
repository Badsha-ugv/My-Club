from django.contrib import admin
from .models import DevDue,DevEvent,DevExpense,DevPayment,DevFund
# Register your models here.



admin.site.register(DevDue)
admin.site.register(DevEvent)
admin.site.register(DevExpense)
admin.site.register(DevPayment)
admin.site.register(DevFund)
