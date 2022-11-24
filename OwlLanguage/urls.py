from django.urls import path
from OwlLanguage import views

urlpatterns = [
    path('',views.homepage,name='home-page'),
    path('about/',views.about_page,name='about-page'),
    path('contact/',views.contact_page,name='contact-page'),
    path('gallery/',views.gallery_page,name='gallery-page'),
    path('album/<int:id>',views.albums_page,name='album-page'),
    path('blogs/',views.blogs_page,name='blogs-page'),
    path('blog-detailes/<str:url>',views.blog_details,name='blog-details'),
    path('products/',views.products_page,name='products-page'),
    path('product-details/<str:url>',views.product_single,name='product-details'),
    path('services/',views.services_page,name='services-page'),
    path('service-details/<str:url>',views.service_details,name='service-details'),
]