from django.shortcuts import render,redirect
from home.models import Service,Contact,Manage_Menu
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
# Create your views here.

@login_required
def services(request):
    service = Service.objects.last()
    contact = Contact.objects.last()
    manage = Manage_Menu.objects.last()

    if service :
        refer_id = ('SE-00%s' %str(service.id+1))
    else :
        refer_id = ('SE-001')

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

        urls = Service.objects.all()

        for u in urls :
            if u.Url == url:
                messages.error(request,'service already exist with same name and url')
                return redirect('services')
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

        Data = Service(Date=date,AddedBy=user,Ip=ip,Title=title,Image=image,Refer_number=refer_id,Description=description,Show_Price=show_price,
        Actual_Price=actual_price,Offer_Price=offer_price,Discount=discount,Show_Whatsapp=whatsapp,Whatsapp_Number=number,
        Show_Enquiry=show_enquiry,Show_Feature=show_feature,Url=url,SMTitle=smtitle,SMDescription=smdescription,SMKeywords=smkeywords)
        Data.save()
        messages.success(request,'new services added successfully')
        return redirect('services')
    
    context = {
        'refer_id' : refer_id,
        'contact' : contact,
        'manage' : manage,
    }
    return render(request,'services.html',context)

########################################################################

@login_required
def manage_service(request):
    services = Service.objects.filter(Status = 1)
    manage = Manage_Menu.objects.last()
    context = {
        'services' : services,
        'manage' : manage,
    }
    return render(request,'manage_service.html',context)

########################################################################

@login_required
def edit_service(request,sid):
    service = Service.objects.get(id=sid)
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
        #     if len(service.Image) > 0:
        #         os.remove(service.Image.path)
            service.Image = request.FILES['image']
        service.EditedBy = user
        service.EditedIp = ip
        service.Edited_Date = datetime.now()
        service.Title = request.POST.get('title')
        service.Description = request.POST.get('description')
        service.Show_Price = request.POST.get('check1')
        service.Actual_Price = request.POST.get('actual_price')
        service.Offer_Price = request.POST.get('offer_price')
        service.Show_Whatsapp = request.POST.get('check2')
        service.Whatsapp_Number = request.POST.get('number')
        service.Show_Enquiry = request.POST.get('check3')
        service.Show_Feature = request.POST.get('check4')
        service.Url = request.POST.get('url')
        service.SMTitle = request.POST.get('smtitle')
        service.SMDescription = request.POST.get('smdescription')
        service.SMKeywords = request.POST.get('smkeywords')
        urls = Service.objects.all()

        for u in urls :
            if u.Url == Service.Url:
                messages.error(request,'service already exist with same name and url')
                return redirect('services')
            else:
                pass
        service.save()
        messages.success(request,'service details edited successfully ...!')
        return redirect('.')
    context = {
        'service' : service,
        'contact' : contact,
        'manage' : manage,
    }
    return render(request,'edit_service.html',context)

########################################################################

@login_required
def remove_service(request,sid):
    service = Service.objects.get(id=sid)

    service.Status = 0
    service.save()
    messages.success(request,'service deleted')
    return redirect('manage_service')

########################################################################

@login_required
def remove_ser_img(request,sid):
    service = Service.objects.get(id=sid)

    service.Image.delete(save=True)
    service.save()

    return redirect('/admin/edit_service/%s' %service.id)