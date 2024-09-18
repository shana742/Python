from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    # Admin URLs
    path('admin/products/', views.admin_product_list, name='admin_product_list'),
    path('admin/products/add/', views.admin_add_product, name='admin_add_product'),
    path('admin/products/add-subcat/', views.admin_add_subcat, name='admin_add_subcat'),
    path('admin/products/edit/<int:pk>/', views.admin_edit_product, name='admin_edit_product'),
    path('admin/products/delete/<int:pk>/', views.admin_delete_product, name='admin_delete_product'),
    # Product Manager URLs
    path('products/search/', views.product_search, name='product_search'),
]
