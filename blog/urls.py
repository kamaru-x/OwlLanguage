from django.urls import path
from blog import views

urlpatterns = [
    path('blog/',views.blog,name='blog'),
    path('manage_blog/',views.manage_blog,name='manage_blog'),
    path('edit_blog/<int:bid>/',views.edit_blog,name='edit_blog'),
    path('remove_blog/<int:bid>/',views.remove_blog,name='remove_blog'),
    path('remove_blog_img/<int:bid>/',views.remove_blog_img,name='remove_img'),
]