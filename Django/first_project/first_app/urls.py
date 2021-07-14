from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('images/', views.show_images, name='images'),
    path('accessRecords/', views.show_access_records, name='records')
]
