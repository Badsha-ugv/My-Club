
from django.contrib import admin
from django.urls import path,include 
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('programming/',include('pro_club.urls')),
    path('development/',include('dev_club.urls')),
    path('account/',include('user_account.urls')),
    path('',include('guest.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
