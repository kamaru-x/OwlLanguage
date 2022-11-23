from django.urls import path
from logos import views

urlpatterns = [
    path('add_logo/',views.add_logo,name='add_logo'),
    path('manage_logo/',views.manage_logo,name='manage_logo'),
    path('remove_logo/<int:lid>/',views.remove_logo,name='remove_logo'),
]