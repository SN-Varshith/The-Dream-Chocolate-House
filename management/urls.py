from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('seasonal-flavors/', views.seasonal_flavor_list, name='seasonal_flavor_list'),
    path('add-seasonal-flavor/', views.add_seasonal_flavor, name='add_seasonal_flavor'),
    path('ingredients/', views.ingredient_list, name='ingredient_list'),
    path('add-ingredient/', views.add_ingredient, name='add_ingredient'),
    path('customer-suggestions/', views.customer_suggestion_list, name='customer_suggestion_list'),
    path('add-customer-suggestion/', views.add_customer_suggestion, name='add_customer_suggestion'),
]
