
from django.contrib import admin
from django.urls import path,include
from core.views import index,contact

urlpatterns = [
     path('', include('core.urls')),
     path('items/',include('items.urls')),
     path('contact/',contact,name='contact'),
     path('admin/', admin.site.urls)
   
]
