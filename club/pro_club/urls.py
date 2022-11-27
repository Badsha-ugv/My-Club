from django.urls import path
from . import views 


urlpatterns  = [
    # path('',views.home,name='home'),
    path('',views.dashboard,name='dashboard'),
    # path('add_member/',views.add_member,name='add_member'),
    path('make_payment/',views.make_payment,name='make_payment'),
    path('expense/',views.expense,name='expense'),
    path('event/',views.event,name='event'),
    path('show_event/',views.show_event,name='show_event'),
    path('complete_event/<str:id>/',views.complete_event,name='complete_event'),
    path('delete_event/<str:id>/',views.delete_event,name='delete_event'),

    path('due_list/', views.due_list, name='due_list'),
    path('payment_history/', views.payment_history, name='payment_history'),
    
    # guest app 
    path('add_gallery_image/',views.add_gallery_image,name='add_gallery_image'),

    path('add_award_event/',views.add_award_event,name='add_award_event'),

    path('create_user_account/',views.create_user_account,name='create_user_account')
    
    
]

