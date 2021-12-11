from django.urls import path
from . import views


app_name = 'notice'

urlpatterns = [
    path('notice/<int:notice_id>', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create', views.create, name="create"),
    path('newnotice/', views.noticepost, name="newnotice"),
    path('', views.notice, name="notice"),
    path('result/', views.result, name="result")
]