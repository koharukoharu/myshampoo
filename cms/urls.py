from django.urls import path
from cms import views


app_name = 'cms'
urlpatterns = [

    path('impression/<int:shampoo_id>/', views.ImpressionList.as_view(), name='impression_list'),
    path('impression/add/<int:shampoo_id>', views.impression_edit, name='impression_add'),
    path('impression/mod/<int:shampoo_id>/<int:impression_id>/', views.impression_edit, name='impression_mod'),  # 修正
    path('impression/del/<int:shampoo_id>/<int:impression_id>/', views.impression_del, name='impression_del'),   # 削除
    path('shampoo/', views.shampoo_list, name='shampoo_list'),
    path('shampoo/add', views.shampoo_edit, name='shampoo_add'),
    path('shampoo/mod/<int:shampoo_id>/', views.shampoo_edit, name='shampoo_mod'),
    path('shampoo/del/<int:shampoo_id>/', views.shampoo_del, name='shampoo_del'),
    
]