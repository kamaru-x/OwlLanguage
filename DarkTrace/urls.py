from django.urls import path
from DarkTrace import views

urlpatterns = [
    path('',views.home_page,name='home-page'),
    path('about/',views.about,name='about-page'),
    path('services/',views.service_page,name='service-page'),
    path('service-details/<str:url>',views.service_details,name='service-details'),
    path('products/',views.product_page,name='product-page'),
    path('product-details/<str:url>',views.product_details,name='product-details'),
    path('blogs/',views.blogs_page,name='blogs-page'),
    path('blog-detailed/<str:url>',views.blog_detailed,name='blog-detailed'),
    path('gallery/',views.gallery_page,name='gallery-page'),
    path('album/<int:id>',views.album_page,name='album-page'),
    path('contact/',views.contact_page,name='contact-page'),
]