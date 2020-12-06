from django.contrib import admin
from django.urls import path,include
from . import views 
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('' , views.index , name = 'index' ),
    path('home/' , views.home , name = 'home' ),
    path('logout/' , views.logout , name = 'logout' ),
    path('detect/' , views.detect , name = 'detect' ),
    path('results/' , views.results , name = 'results' ),
    path('recommend/' , views.recommend , name = 'recommend'),
    path('history/' , views.history , name = 'history'),
    path('shistory/' , views.shistory , name = 'shistory'),
    path('contact/' , views.contact , name = 'contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)