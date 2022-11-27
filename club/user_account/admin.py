from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser 

# Register your models here.

class CustomAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets +(
        (None, {'fields': ('student_id', 'phone_number', 'batch',
         'semester', 'address', 'gender', 'user_type', 'club_name', 'profile_pic')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets +(
        (None, {'fields': ('student_id', 'phone_number', 'batch',
         'semester', 'address', 'gender', 'user_type', 'club_name', 'profile_pic')}),
    )

admin.site.register(CustomUser,CustomAdmin) 
