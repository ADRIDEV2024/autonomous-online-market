from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', list_categories, name='list_categories'),
    path('categories/<int:pk>/', category_detail, name='category_detail'),
    path('categories/create/', create_category, name='create_category'),
    path('categories/update/<int:pk>/', update_category, name='update_category'),
    path('categories/delete/<int:pk>/', delete_category, name='delete_category'),

    path('product/', view_products, name='view_products'),
    path('product/<int:pk>/', view_product_detail, name='view_product_detail'),
    path('product/create/', add_product, name='add_product'),
    path('product/update/<int:pk>/', update_product, name='update_product'),
    path('product/delete/<int:pk>/', delete_product, name='delete_product'),
    path('', api_overview, name='api_overview'),
]
