from django.urls import path
from app2.views import *

app_name = 'Nothing'

urlpatterns = [
    path('third/', third, name = 'third'),
    path('third1/', third1, name='third1'),
    path('fourth/', fourth, name='fourth'),
    path('fourth1/', fourth1, name='fourth1'),
]