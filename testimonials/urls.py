from django.urls import path
from testimonials import views

urlpatterns = [
    path('add_testimonial/',views.add_testimonial,name='add_testimonial'),
    path('manage_testimonial/',views.manage_testimonial,name='manage_testimonial'),
    path('edit_testimonial/<int:tid>/',views.edit_testimonial,name='edit_testimonial'),
    path('remove_testimonial/<int:tid>/',views.remove_testimonial,name='remove_testimonial'),
    path('remove_tes_img/<int:tid>/',views.remove_tes_img,name='remove_tes_img'),
]