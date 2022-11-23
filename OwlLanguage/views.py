from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,'fp/index.html')

def header(request):
    return render(request,'fp/header.html')

def footer(request):
    return render(request,'fp/footer.html')

def about_page(request):
    return render(request,'fp/about.html')

def albums_page(request):
    return render(request,'fp/album.html')

def gallery_page(request):
    return render(request,'fp/gallery.html')

def blogs_page(request):
    return render(request,'fp/blog.html')

def blog_details(request):
    return render(request,'fp/blog-single.html')

def contact_page(request):
    return render(request,'fp/contact.html')

def products_page(request):
    return render(request,'fp/products.html')

def product_single(request):
    return render(request,'fp/products-single.html')

def services_page(request):
    return render(request,'fp/service.html')

def service_details(request):
    return render(request,'fp/service-single.html')