from django.urls import path
from banners import views

urlpatterns = [
    path('banner/',views.banner,name='banner'),
    path('manage_banner/',views.manage_banner,name='manage_banner'),
    path('edit_banner/<int:bid>/',views.edit_banner,name='edit_banner'),
    path('remove_banner/<int:bid>/',views.remove_banner,name='remove_banner'),
    path('remove_ban_img/<int:bid>/',views.remove_ban_img,name='remove_ban_img')
]