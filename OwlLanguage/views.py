from django.shortcuts import render,redirect
from home.models import Feedback,About,Blog,Album,Album_Image,Contact,Product,Service,Enquiry,Manage_Menu,Quick_Links,Group_Of_Companies,Testimonial,Banners,Theme
from datetime import datetime
# Create your views here.

def homepage(request):
    manage = Manage_Menu.objects.last()
    quick = Quick_Links.objects.last()
    products = Product.objects.filter(Show_Feature=1)
    services = Service.objects.filter(Show_Feature=1)
    contact = Contact.objects.last()
    banners = Banners.objects.filter(Status=1)
    about = About.objects.last()
    blogs = Blog.objects.filter(Status=1).order_by('-id')[:3]
    testimonial = Testimonial.objects.filter(Status=1)
    goc = Group_Of_Companies.objects.filter(Status=1)
    color = Theme.objects.last()
    context = {
        'manage' : manage,
        'quick' : quick,
        'products' : products,
        'services' : services,
        'contact' : contact,
        'banners' : banners,
        'about' : about,
        'blogs' : blogs,
        'testimonials' : testimonial,
        'goc' : goc,
        'color' : color
    }
    return render(request,'fp/index.html',context)

##################################################################################################################

def header(request):
    manage = Manage_Menu.objects.last()
    quick = Quick_Links.objects.last()
    products = Product.objects.filter(Status=1)
    services = Service.objects.filter(Status=1)
    contact = Contact.objects.last()
    color = Theme.objects.last()
    context = {
        'manage' : manage,
        'quick' : quick,
        'products' : products,
        'services' : services,
        'contact' : contact,
        'color' : color
    }
    return render(request,'fp/header.html',context)

##################################################################################################################

def footer(request):
    manage = Manage_Menu.objects.last()
    quick = Quick_Links.objects.last()
    products = Product.objects.filter(Status=1).filter(Show_Feature=1)
    services = Service.objects.filter(Status=1).filter(Show_Feature=1)
    contact = Contact.objects.last()
    color = Theme.objects.last()
    context = {
        'manage' : manage,
        'quick' : quick,
        'products' : products,
        'services' : services,
        'contact' : contact,
        'color' : color
    }
    return render(request,'fp/footer.html',context)

##################################################################################################################

def about_page(request):
    manage = Manage_Menu.objects.last()
    quick = Quick_Links.objects.last()
    products = Product.objects.filter(Status=1)
    services = Service.objects.filter(Status=1)
    contact = Contact.objects.last()
    about = About.objects.last()
    color = Theme.objects.last()
    context = {
        'manage' : manage,
        'quick' : quick,
        'products' : products,
        'services' : services,
        'contact' : contact,
        'about' : about,
        'color' : color
    }
    return render(request,'fp/about.html',context)

##################################################################################################################

def albums_page(request,id):
    manage = Manage_Menu.objects.last()
    quick = Quick_Links.objects.last()
    products = Product.objects.filter(Status=1)
    services = Service.objects.filter(Status=1)
    contact = Contact.objects.last()
    images = Album_Image.objects.filter(Album_Name=id).filter(Status=1)
    color = Theme.objects.last()
    context = {
        'manage' : manage,
        'quick' : quick,
        'products' : products,
        'services' : services,
        'contact' : contact,
        'images' : images,
        'color' : color
    }
    return render(request,'fp/album.html',context)

##################################################################################################################

def gallery_page(request):
    manage = Manage_Menu.objects.last()
    quick = Quick_Links.objects.last()
    products = Product.objects.filter(Status=1)
    services = Service.objects.filter(Status=1)
    contact = Contact.objects.last()
    albums = Album.objects.filter(Status=1)
    color = Theme.objects.last()
    context = {
        'manage' : manage,
        'quick' : quick,
        'products' : products,
        'services' : services,
        'contact' : contact,
        'albums' : albums,
        'color' : color
    }
    return render(request,'fp/gallery.html',context)

##################################################################################################################

def blogs_page(request):
    manage = Manage_Menu.objects.last()
    quick = Quick_Links.objects.last()
    products = Product.objects.filter(Status=1)
    services = Service.objects.filter(Status=1)
    contact = Contact.objects.last()
    blogs = Blog.objects.filter(Status=1)
    color = Theme.objects.last()
    context = {
        'manage' : manage,
        'quick' : quick,
        'products' : products,
        'services' : services,
        'contact' : contact,
        'blogs' : blogs,
        'color' : color
    }
    return render(request,'fp/blog.html',context)

##################################################################################################################

def blog_details(request,url):
    manage = Manage_Menu.objects.last()
    quick = Quick_Links.objects.last()
    products = Product.objects.filter(Status=1)
    services = Service.objects.filter(Status=1)
    contact = Contact.objects.last()
    blog = Blog.objects.get(Url=url)
    color = Theme.objects.last()

    context = {
        'manage' : manage,
        'quick' : quick,
        'products' : products,
        'services' : services,
        'contact' : contact,
        'blog' : blog,
        'color' : color
    }
    return render(request,'fp/blog-single.html',context)

##################################################################################################################

def contact_page(request):
    manage = Manage_Menu.objects.last()
    quick = Quick_Links.objects.last()
    products = Product.objects.filter(Status=1)
    services = Service.objects.filter(Status=1)
    contact = Contact.objects.last()
    color = Theme.objects.last()
    context = {
        'manage' : manage,
        'quick' : quick,
        'products' : products,
        'services' : services,
        'contact' : contact,
        'color' : color
    }
    return render(request,'fp/contact.html',context)

##################################################################################################################

def products_page(request):
    manage = Manage_Menu.objects.last()
    quick = Quick_Links.objects.last()
    products = Product.objects.filter(Status=1)
    services = Service.objects.filter(Status=1)
    contact = Contact.objects.last()
    color = Theme.objects.last()
    context = {
        'manage' : manage,
        'quick' : quick,
        'products' : products,
        'services' : services,
        'contact' : contact,
        'color' : color
    }
    return render(request,'fp/products.html',context)

##################################################################################################################

def product_single(request,url):
    manage = Manage_Menu.objects.last()
    quick = Quick_Links.objects.last()
    products = Product.objects.filter(Status=1)
    services = Service.objects.filter(Status=1)
    contact = Contact.objects.last()
    product = Product.objects.get(Url=url)
    color = Theme.objects.last()

    if request.method == 'POST' :
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')

        product_name = product.Title
        product_ref = product.Refer_number
        date = datetime.now()
        x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forw_for is not None:
            ip = x_forw_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        data = Enquiry(Name=name,Mobile_Number=mobile,Email=email,Product_Name=product_name,Refer_number=product_ref,Date=date,Ip=ip)
        data.save()
        return redirect('/product-details/%s' %product.Url)

    context = {
        'manage' : manage,
        'quick' : quick,
        'products' : products,
        'services' : services,
        'contact' : contact,
        'product' : product,
        'color' : color
    }
    return render(request,'fp/products-single.html',context)

##################################################################################################################

def services_page(request):
    manage = Manage_Menu.objects.last()
    quick = Quick_Links.objects.last()
    products = Product.objects.filter(Status=1)
    services = Service.objects.filter(Status=1)
    contact = Contact.objects.last()
    color = Theme.objects.last()
    context = {
        'manage' : manage,
        'quick' : quick,
        'products' : products,
        'services' : services,
        'contact' : contact,
        'color' : color
    }
    return render(request,'fp/service.html',context)

##################################################################################################################

def service_details(request,url):
    manage = Manage_Menu.objects.last()
    quick = Quick_Links.objects.last()
    products = Product.objects.filter(Status=1)
    services = Service.objects.filter(Status=1)
    contact = Contact.objects.last()
    service = Service.objects.get(Url=url)
    color = Theme.objects.last()

    if request.method == 'POST' :
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')

        service_name = service.Title
        service_ref = service.Refer_number
        date = datetime.now()
        x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forw_for is not None:
            ip = x_forw_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        data = Enquiry(Name=name,Mobile_Number=mobile,Email=email,Product_Name=service_name,Refer_number=service_ref,Date=date,Ip=ip)
        data.save()
        return redirect('/service-details/%s' %service.Url)

    context = {
        'manage' : manage,
        'quick' : quick,
        'products' : products,
        'services' : services,
        'contact' : contact,
        'service' : service,
        'color' : color
    }
    return render(request,'fp/service-single.html',context)