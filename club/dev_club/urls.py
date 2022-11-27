from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.dev_dashboard, name='dev_dashboard'),
    
    path('make_payment/', views.dev_make_payment, name='dev_make_payment'),
    path('expense/', views.dev_expense, name='dev_expense'),
    path('event/', views.dev_event, name='dev_event'),
    path('show_event/', views.dev_show_event, name='dev_show_event'),
    path('complete_event/<str:id>/',
         views.dev_complete_event, name='dev_complete_event'),
    path('delete_event/<str:id>/',
         views.dev_delete_event, name='dev_delete_event'),

    


    path('due_list/', views.due_list, name='dev_due_list'),
    path('payment_history/', views.payment_history, name='dev_payment_history'),

    # guest app
    path('add_gallery_image/', views.add_gallery_image,
         name='dev_add_gallery_image'),

    path('add_award_event/', views.add_award_event, name='dev_add_award_event'),

    path('create_user_account/', views.create_user_account,
         name='dev_create_user_account')
]