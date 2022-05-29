"""IDS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Apps.home import views as home_views
from Apps.Signup import views as Signup_views
from Apps.Dashboard import urls as Dash_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , home_views.home , name='home' ),
    path('Signin/' , Signup_views.signin , name='Signin' ),
    path('Signup/' , Signup_views.signup , name='Signup'),
    path('Signout/', Signup_views.logout , name='logout'),
    path('Dashboard/', include(Dash_urls.urlpatterns) ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
