from django.urls import path
from cms import views


app_name = 'cms'
urlpatterns = [

    path('shampoo/', views.shampoo_list, name='shampoo_list'),
    path('shampoo/add', views.shampoo_edit, name='shampoo_add'),
    path('shampoo/mod/<int:shampoo_id>/', views.shampoo_edit, name='shampoo_mod'),
    path('shampoo/del/<int:shampoo_id>/', views.shampoo_del, name='shampoo_del'),
    
]