from django.urls import path 
from . import views 

urlpatterns = [ 
    path('',views.home, name='home'),
    # path('guest_register/', views.guest_register, name='guest_register'),
    # path('guest_login/',views.guest_login, name='guest_login'),
    path('guest_logout/', views.guest_logout, name='guest_logout'),

    path('project/',views.project, name='project'),
    path('people/',views.people, name='people'),
    path('award/',views.award, name='award'),
    path('gallery/',views.gallery,name='gallery'),

    path('profile/<str:id>/',views.profile, name='profile'),

    #create project 
    path('create_project/',views.create_project, name='create_project'),
    path('project_view/<str:id>/',views.project_view, name='project_view'),

    #award
    path('award_view/<str:id>/', views.award_view, name='award_view'),

    #update profile 
    path('update_profile/<str:id>/', views.update_profile,name='update_profile'),
    



    
]