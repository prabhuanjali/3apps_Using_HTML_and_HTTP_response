from django.urls import path
from app3.views import *

app_name = 'Anything'

urlpatterns = [
    path('fifth/', fifth, name = 'fifth'),
    path('fifth1/', fifth1, name='fifth1'),
    path('sixth/', sixth, name='sixth'),
    path('sixth1/', sixth1, name='sixth1'),
]