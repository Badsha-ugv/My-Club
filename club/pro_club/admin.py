from django.contrib import admin
from .models import  Fund, Expense, Payment, Event, Due

# Register your models here.


admin.site.register(Fund)
admin.site.register(Expense)
admin.site.register(Payment)
admin.site.register(Event)
admin.site.register(Due)
