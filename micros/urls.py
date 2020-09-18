from django.urls import path
from . import views


app_name = 'micros'

urlpatterns = [
    path('', views.home, name='home'),
]
