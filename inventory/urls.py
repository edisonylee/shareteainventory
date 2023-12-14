from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.list_boba_products, name='list_boba_products'),
]