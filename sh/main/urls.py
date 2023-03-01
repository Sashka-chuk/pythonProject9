from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='base'),
    path('post/', post, name='post'),
    path('get/', get, name='get'),
    path('reg/', reg, name='reg')
]
