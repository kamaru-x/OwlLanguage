from django.shortcuts import render,redirect
from home.models import Contact,Enquiry,Manage_Menu,Product,Quick_Links,Service,Feedback,About,Blog,Album,Theme
from home.forms import AboutForm
from django.contrib import messages
import os
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from datetime import datetime
import xlwt
# Create your views here.

########################################################################

def index(request):
    manage = Manage_Menu.objects.last()
    context = {
        'manage' : manage
    }
    return render(request,'index.html',context)

########################################################################

def test_area(request):
    user = request.user.id
    print(user)
    return render(request,'test-area.html')

########################################################################

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request,'incorrect email or password')
            return redirect('.')
    return render(request,'login.html')

########################################################################

@login_required
def dashboard(request):
    feedbacks = Feedback.objects.all()
    products = Product.objects.all()
    services = Service.objects.all()
    blogs = Blog.objects.all()
    albums = Album.objects.all()
    manage = Manage_Menu.objects.last()

    product_count = len(products)
    service_count = len(services)
    blog_count = len(blogs)
    album_count = len(albums)

    context = {
        'feedbacks':feedbacks,
        'pro' : product_count,
        'ser' : service_count,
        'blg' : blog_count,
        'alb' : album_count,
        'manage' : manage,
    }
    return render(request,'dashboard.html',context,)

########################################################################

@login_required
def about_us(request):
    about = About.objects.last()
    manage = Manage_Menu.objects.last()
    form = AboutForm
    if request.method == "POST":
        if about :
            form = AboutForm(request.POST , request.FILES , instance=about)
        else:
            form = AboutForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'about edited successfully')
            return redirect('about_us')
    form = AboutForm(instance=about)
    context = {
        'about' : about,
        'form' : form,
        'manage' : manage,
    }
    return render(request,'about_us.html',context)

########################################################################

@login_required
def contact_us(request):
    contact = Contact.objects.last()
    manage = Manage_Menu.objects.last()

    user = request.user.id

    date = datetime.now()
        
    x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forw_for is not None:
        ip = x_forw_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    if request.method == 'POST':
        if contact:
            if len(request.FILES) != 0:
        #         if len(contact.Image) > 0:
        #             os.remove(contact.Image.path)
                contact.Image = request.FILES['image']
            contact.EditedBy = user
            contact.EditedIp = ip
            contact.Edited_Date = datetime.now()
            contact.Company_Name = request.POST.get('title')
            contact.Mobile = request.POST.get('mobile')
            contact.Telephone = request.POST.get('telephone')
            contact.Email = request.POST.get('email')
            contact.Website = request.POST.get('website')
            contact.Adress = request.POST.get('address')
            contact.Latitude = request.POST.get('latitude')
            contact.Longitude = request.POST.get('longitude')
            contact.Whatsapp = request.POST.get('whatsapp')
            contact.Facebook = request.POST.get('facebook')
            contact.Url = request.POST.get('url')
            contact.Instagram = request.POST.get('instagram')
            contact.Twitter = request.POST.get('twitter')
            contact.Linkedin = request.POST.get('linkedin')
            contact.SMTitle = request.POST.get('smtitle')
            contact.SMDescription = request.POST.get('smdescription')
            contact.SMKeywords = request.POST.get('smkeywords')
            contact.save()
            messages.success(request,'contact details edited successfully ...!')
            return redirect('contact_us')
        else:
            image = request.FILES['image']
            title = request.POST.get('title')
            mobile = request.POST.get('mobile')
            telephone = request.POST.get('telephone')
            email = request.POST.get('email')
            website = request.POST.get('website')
            address = request.POST.get('address')
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
            whatsapp = request.POST.get('whatsapp')
            facebook = request.POST.get('fecebook')
            url = request.POST.get('url')
            instagram = request.POST.get('instagram')
            twitter = request.POST.get('twitter')
            linkedin = request.POST.get('linkedin')
            smtitle = request.POST.get('smtitle')
            smdescription = request.POST.get('smdescription')
            smkeywords = request.POST.get('smkeywords')

            user = request.user.id
        
            x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forw_for is not None:
                ip = x_forw_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')

            data = Contact(Date=date,AddedBy=user,Ip=ip,Company_Name=title,Adress=address,Telephone=telephone,
            Mobile=mobile,Whatsapp=whatsapp,Email=email,Website=website,Longitude=longitude,
            Latitude=latitude,Facebook=facebook,Instagram=instagram,Linkedin=linkedin,
            Twitter=twitter,Image=image,Url=url,SMTitle=smtitle,SMDescription=smdescription,SMKeywords=smkeywords)
            data.save()
            return redirect('contact_us')
    return render(request,'contact_us.html',{'data':contact,'manage':manage})

########################################################################

@login_required
def feedback(request):
    feedbacks = Feedback.objects.filter(Status = 1)
    manage = Manage_Menu.objects.last()
    context = {
        'feedbacks' : feedbacks,
        'manage' : manage
    }
    return render(request,'feedback.html',context)

########################################################################

@login_required
def enquiry(request):
    enquiries = Enquiry.objects.filter(Status = 1)
    manage = Manage_Menu.objects.last()
    context = {
        'enquiries' : enquiries,
        'manage' : manage
    }
    return render(request,'enquiry.html',context)

########################################################################

@login_required
def view_enquiry(request,eid):
    enquiry = Enquiry.objects.get(id=eid)
    context = {
        'enquiry' : enquiry,
    }
    return render(request,'view_enquiry.html',context)

########################################################################

@login_required
def manage_menu(request):
    manage = Manage_Menu.objects.last()

    user = request.user.id
        
    x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forw_for is not None:
        ip = x_forw_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    if request.method == 'POST':
        if manage:
            manage.About_Page = request.POST.get('about')
            manage.Blog_Page = request.POST.get('blog')
            manage.Image_Gallery = request.POST.get('gallery')
            manage.Contact_Page = request.POST.get('contact')
            manage.Products_Page = request.POST.get('products')
            manage.Service_Page = request.POST.get('services')
            manage.Testimonials = request.POST.get('testimonials')
            manage.Feedback_Page = request.POST.get('feedback')
            manage.Enquiry_Page = request.POST.get('enquiry')
            manage.Group_Company = request.POST.get('gop')
            manage.EditedBy = user
            manage.Edited_Date = datetime.now()
            manage.EditedIp = ip
            manage.save()
            
            messages.success(request,'manage manu edited successfully ...!')
            return redirect('manage_menu')
        else:
            about = request.POST.get('about')
            blog = request.POST.get('blog')
            gallery = request.POST.get('gallery')
            contact = request.POST.get('contact')
            products = request.POST.get('products')
            services = request.POST.get('services')
            testimonials = request.POST.get('testimonials')
            feedback = request.POST.get('feedback')
            enquiry = request.POST.get('enquiry')
            gop = request.POST.get('gop')

            user = request.user.id

            date = datetime.now()
        
            x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forw_for is not None:
                ip = x_forw_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
            
            data = Manage_Menu(Date=date,AddedBy=user,Ip=ip,About_Page=about,Blog_Page=blog,Image_Gallery=gallery,Contact_Page=contact,
            Products_Page=products,Service_Page=services,Testimonials=testimonials,Feedback_Page=feedback,
            Enquiry_Page=enquiry,Group_Company=gop)
            data.save()
            
            messages.success(request,'manage manu edited successfully ...!')
            return redirect('manage_menu')
    context = {
        'manage' : manage,
    }
    return render(request,'manage_menu.html',context)

########################################################################

@login_required
def quick_links(request):
    quick = Quick_Links.objects.last()
    manage = Manage_Menu.objects.last()

    user = request.user.id
        
    x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forw_for is not None:
        ip = x_forw_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    if request.method == 'POST':
        if quick :
            quick.About_Page = request.POST.get('about')
            quick.Blog_Page = request.POST.get('blog')
            quick.Image_Gallery = request.POST.get('gallery')
            quick.Contact_Page = request.POST.get('contact')
            quick.Products_Page = request.POST.get('products')
            quick.Service_Page = request.POST.get('services')
            quick.Testimonials = request.POST.get('testimonials')
            quick.Optional_Products = request.POST.get('op-products')
            quick.Optional_Service = request.POST.get('op-services')
            quick.EditedBy = user
            quick.EditedIp = ip
            quick.Edited_Date = datetime.now()
            quick.save()
            messages.success(request,'quick links edited successfully ...!')
            return redirect('quick_links')
        else:
            about = request.POST.get('about')
            blog = request.POST.get('blog')
            gallery = request.POST.get('gallery')
            contact = request.POST.get('contact')
            products = request.POST.get('products')
            services = request.POST.get('services')
            testimonials = request.POST.get('testimonials')
            op_products = request.POST.get('op-products')
            op_services = request.POST.get('op-services')

            user = request.user.id

            date = datetime.now()
        
            x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forw_for is not None:
                ip = x_forw_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')

            data = Quick_Links(Date=date,AddedBy=user,Ip=ip,About_Page=about,Blog_Page=blog,Image_Gallery=gallery,Contact_Page=contact,
            Products_Page=products,Service_Page=services,Testimonials=testimonials,Optional_Products=op_products,Optional_Service=op_services)
            data.save()
            messages.success(request,'quick links edited successfully ...!')
            return redirect('quick_links')
    context = {
        'quick' : quick,
        'manage' : manage,
    }
    return render(request,'quick_links.html',context)

########################################################################

@login_required
def remove_abt_img(request,aid):
    about = About.objects.get(id=aid)

    about.Image.delete(save=True)
    about.save()

    return redirect('/admin/about_us')

########################################################################

@login_required
def remove_feedback(request,fid):
    feedback = Feedback.objects.get(id=fid)
    feedback.Status = 0
    feedback.save()
    return redirect('feedback')

########################################################################

@login_required
def remove_enquiry(request,eid):
    enquiry = Enquiry.objects.get(id=eid)
    enquiry.Status = 0
    enquiry.save()
    return redirect('enquiry')

########################################################################

@login_required
def user_profile(request):
    manage = Manage_Menu.objects.last()
    form = UserChangeForm
    if request.method == "POST":
        form = AboutForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'about edited successfully')
            return redirect('about_us')
    form = UserChangeForm()
    context = {
        'form' : form,
        'manage' : manage
    }
    return render(request,'change-password.html',context)

########################################################################

@login_required
def signout(request):
    logout(request)
    return redirect('/')

########################################################################

@login_required
def change_color(request):
    color = Theme.objects.last()
    manage = Manage_Menu.objects.last()

    user = request.user.id
        
    x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forw_for is not None:
        ip = x_forw_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    if request.method == 'POST' :
        color.Primary = request.POST.get('primary')
        color.Secondary = request.POST.get('secondary')
        color.EditedBy = user
        color.EditedIp = ip
        color.Edited_Date = datetime.now()
        color.save()
        return redirect('/admin/theme')
    context ={
        'color' : color,
        'manage' : manage
    }
    return render(request,'change-theme.html',context)

########################################################################

def export_feedbacks(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Feedbacks' + str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Feedbacks')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Date','Name','Email','Contact','Website','Message']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    font_style = xlwt.XFStyle()

    rows = Feedback.objects.all().values_list('Date','Name','Email','Contact','Website','Message')

    for row in rows:
        row_num+=1

        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)
    wb.save(response)

    return response

########################################################################

def export_enquiries(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Enquiries' + str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Enquiries')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Date','Name','Mobile_Number','Email','Product_Name','Refer_number','Whatsapp','District','Address']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    font_style = xlwt.XFStyle()

    rows = Enquiry.objects.all().values_list('Date','Name','Mobile_Number','Email','Product_Name','Refer_number','Whatsapp','District','Address')

    for row in rows:
        row_num+=1

        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)
    wb.save(response)

    return response