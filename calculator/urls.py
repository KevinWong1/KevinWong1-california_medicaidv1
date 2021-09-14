from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = "calculator"

urlpatterns = [
    path('calculator', views.index, name='index')
]
