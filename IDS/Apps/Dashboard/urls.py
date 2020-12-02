from django.contrib import admin
from django.urls import path,include
from . import views 
urlpatterns = [
    path('' , views.index , name = 'index' ),
    path('home/' , views.home , name = 'home' ),
    path('logout/' , views.logout , name = 'logout' ),
    path('detect/' , views.detect , name = 'detect' ),
    path('results/' , views.results , name = 'results' ),
]