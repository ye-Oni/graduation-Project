from django.urls import path
from .views import *


app_name = 'recommendApp'

urlpatterns = [
    path('',recommend_index,name='recommend_index'),
    path('result/',recommend_new, name='recommend_result'),

]