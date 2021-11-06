from django.urls import path
from . import views
urlpatterns = [
     path('', views.index, name='index'),
     path('contact', views.contact, name='contact'),
     path('property-grid', views.propertyGrid, name='property-grid'),
     path('property-detail/<int:id>', views.propertyDetail, name='property-detail'),
     path('about', views.about, name='about'),
     path('agents', views.agents, name='agents'),
     path('offplan', views.offplan, name='offplan'),
     path('offplandetail', views.offplandetail, name='offplandetail'),
]
