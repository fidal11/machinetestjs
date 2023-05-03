from django.urls import path
from .import views

urlpatterns = [
    path('kseb',views.kseb,name='kseb'),  

]