from django.urls import path
from products import views

urlpatterns = [
    path('products/',views.products,name='products'),
    path('manage_product/',views.manage_product,name='manage_product'),
    path('edit_product/<int:pid>/',views.edit_product,name='edit_product'),
    path('remove_product/<int:pid>/',views.remove_product,name='remove_product'),
    path('remove_pro_img/<int:pid>/',views.remove_pro_img,name='remove_pro_img')
]