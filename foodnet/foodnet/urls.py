"""foodnet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from catalog import views
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
# from django.contrib.auth.urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginUser.as_view(), name='login'),
    path('', views.IndexView.as_view(), name='index'),
    path('top/', views.top, name="top"),
    path('addRecipe/', views.AddRecipe.as_view(), name="addRecipe"),
    path('accounts/register/', views.RegisterUser.as_view(), name='register'),

]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
