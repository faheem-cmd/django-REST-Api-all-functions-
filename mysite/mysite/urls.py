"""myapi URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from webapp import views
from webapp.views import CartItemViews, CarsAPIView
from webapp.views import RegisterAPI
from knox import views as knox_views
from webapp.views import LoginAPI

urlpatterns = [
    path('', admin.site.urls),
    path('news/', views.newsList.as_view()),
    path('workers/', views.workersList.as_view()),
    path('cars/', CarsAPIView.as_view()),
    path('cart-items/', CartItemViews.as_view()),
    path('registers/', RegisterAPI.as_view(), name='register'),
    path('logins/', LoginAPI.as_view(), name='login'),
    path('logouts/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    re_path(r'^static/(?P<path>.*)/$', serve,
            {'document_root': settings.STATICFILES_DIRS}),
    re_path(r'^media/(?P<path>.*)/$', serve,
            {'document_root': settings.MEDIA_ROOT}),

]
