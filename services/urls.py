from django.urls import path
from services import views

urlpatterns = [
    path('services/',views.services,name='services'),
    path('manage_service/',views.manage_service,name='manage_service'),
    path('edit_service/<int:sid>/',views.edit_service,name='edit_service'),
    path('remove_service/<int:sid>/',views.remove_service,name='remove_service'),
    path('remove_ser_img/<int:sid>/',views.remove_ser_img,name='remove_ser_img'),
]