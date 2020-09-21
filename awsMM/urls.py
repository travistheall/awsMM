"""awsMM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# Django main imports
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# Django Rest Framework imports
from rest_framework import routers
# My imports
from micros import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)
router.register('maindesc', views.MainfooddescSearchView)
router.register('adddesc', views.AddfooddescSearchView)
router.register('weights', views.FoodweightsSearchView)
router.register('portiondesc', views.FoodportiondescSearchView)
router.register('nutvalabb', views.FnddsnutvalAbbrevSearchView)
router.register('nutdesc', views.NutdescSearchView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('micros.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
