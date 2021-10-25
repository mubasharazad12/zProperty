from django.urls import path
from . import views
urlpatterns = [
     path('', views.index, name='index'),
     path('contact', views.contact, name='contact'),
     path('property-grid', views.propertyGrid, name='property-grid'),
     path('property-detail', views.propertyDetail, name='property-detail'),
]
