from django.urls import path

from app1.views import *

app_name= 'Anything'


urlpatterns = [
    path('first/', first, name='first'),
    path('first1/', first1, name='first1'),
    path('second/', second, name='second'),
    path('second1/', second1, name='second1'),
]