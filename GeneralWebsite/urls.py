"""GeneralWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dbadmin/', admin.site.urls),
    path('',include('DarkTrace.urls')),
    path('admin/',include('home.urls')),
    path('admin/',include('blog.urls')),
    path('admin/',include('gallery.urls')),
    path('admin/',include('logos.urls')),
    path('admin/',include('products.urls')),
    path('admin/',include('services.urls')),
    path('admin/',include('testimonials.urls')),
    path('admin/',include('banners.urls')),
    path('admin/',include('django.contrib.auth.urls')),
    path('ckeditor/',include('ckeditor_uploader.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)