from django.urls import path
from .views import *


app_name = 'c_type'

urlpatterns = [
    path('',index,name='index'),
    path('result/',result, name='result'),

]