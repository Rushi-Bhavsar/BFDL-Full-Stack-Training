from django.urls import path
from . import views

app_name = 'fourth_app'
urlpatterns = [
    path('other/', views.other, name='other'),
    path('relative/', views.relative_url, name='relative_url')

]
