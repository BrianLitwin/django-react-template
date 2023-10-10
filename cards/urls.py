# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.SimpleEndpoint.as_view(), name='simple_endpoint'),
]