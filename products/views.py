from django.shortcuts import render,redirect
from home.models import Product,Contact,Manage_Menu
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.

@login_required
def products(request):
    product = Product.objects.last()
    contact = Contact.objects.last()
    manage = Manage_Menu.objects.last()

    if product :
        refer_id = ('PR-00%s' %str(product.id+1))
    else :
        refer_id = ('PR-001')


    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES['image']
        description = request.POST.get('description')
        show_price = request.POST.get('check1')
        whatsapp = request.POST.get('check2')
        show_enquiry = request.POST.get('check3')
        show_feature = request.POST.get('check4')
        actual_price = request.POST.get('actual_price')
        offer_price = request.POST.get('offer_price')
        number = request.POST.get('number')
        url = request.POST.get('url')
        smtitle = request.POST.get('smtitle')
        smkeywords = request.POST.get('smkeywords')
        smdescription = request.POST.get('smdescription')

        urls = Product.objects.all()

        for u in urls :
            if u.Url == url:
                messages.error(request,'product already exist with same name and url')
                return redirect('products')
            else:
                pass

        discount = (int(actual_price) - int(offer_price)) / int(actual_price) * 100

        user = request.user.id

        date = datetime.now()
        
        x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forw_for is not None:
            ip = x_forw_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        Data = Product(Date=date,AddedBy=user,Ip=ip,Title=title,Image=image,Refer_number=refer_id,Description=description,Show_Price=show_price,
        Actual_Price=actual_price,Offer_Price=offer_price,Discount=discount,Show_Whatsapp=whatsapp,Whatsapp_Number=number,
        Show_Enquiry=show_enquiry,Show_Feature=show_feature,Url=url,SMTitle=smtitle,SMDescription=smdescription,SMKeywords=smkeywords)
        Data.save()
        messages.success(request,'added new product succesfully')
        return redirect('products')

    context = {
        'refer_id' : refer_id,
        'contact' : contact,
        'manage' : manage,
    }

    return render(request,'products.html',context)

########################################################################

@login_required
def manage_product(request):
    products = Product.objects.filter(Status = 1)
    manage = Manage_Menu.objects.last()
    context = {
        'products' : products,
        'manage' : manage,
    }
    return render(request,'manage_product.html',context)

########################################################################

@login_required
def edit_product(request,pid):
    product = Product.objects.get(id=pid)
    contact = Contact.objects.last()
    manage = Manage_Menu.objects.last()

    user = request.user.id
        
    x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forw_for is not None:
        ip = x_forw_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    if request.method == 'POST':
        if len(request.FILES) != 0:
        #     if len(product.Image) > 0:
        #         os.remove(product.Image.path)
            product.Image = request.FILES['image']
        product.EditedBy = user
        product.EditedIp = ip
        product.Edited_Date = datetime.now()
        product.Title = request.POST.get('title')
        product.Description = request.POST.get('description')
        product.Show_Price = request.POST.get('check1')
        product.Actual_Price = request.POST.get('actual_price')
        product.Offer_Price = request.POST.get('offer_price')
        product.Show_Whatsapp = request.POST.get('check2')
        product.Whatsapp_Number = request.POST.get('number')
        product.Show_Enquiry = request.POST.get('check3')
        product.Show_Feature = request.POST.get('check4')
        product.Url = request.POST.get('url')
        product.SMTitle = request.POST.get('smtitle')
        product.SMDescription = request.POST.get('smdescription')
        product.SMKeywords = request.POST.get('smkeywords')
        product.save()
        messages.success(request,'product details edited successfully')
        return redirect('.')
    context = {
        'product' : product,
        'contact' : contact,
        'manage' : manage,
    }
    return render(request,'edit_product.html',context)

########################################################################

@login_required
def remove_product(request,pid):
    product = Product.objects.get(id=pid)

    product.Status = 0
    product.save()
    messages.success(request,'product deleted successfully')
    return redirect('manage_product')

########################################################################

@login_required
def remove_pro_img(request,pid):
    product = Product.objects.get(id=pid)

    product.Image.delete(save=True)
    product.save()

    return redirect('/admin/edit_product/%s' %product.id)