from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home Page'),
    path('about/', views.about, name='About'),
    path('dashboard/offer/', views.offer, name='Offer'),
    path('dashboard/offer/food_offered/', views.food_offered, name='food_offered'),
    path('dashboard/status/', views.status, name='Status')
    
    

]
