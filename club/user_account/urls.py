from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.pc_login,name='pc_login'),
    path('pc_logout/',views.pc_logout,name='pc_logout'),

    
    
]