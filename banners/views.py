from django.shortcuts import render,redirect
from home.models import Banners,Manage_Menu
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.

@login_required
def banner(request):
    manage = Manage_Menu.objects.last()
    if request.method == 'POST' :
        caption = request.POST.get('caption')
        scaption = request.POST.get('scaption')
        label = request.POST.get('label')
        link = request.POST.get('link')
        image = request.FILES['image']

        user = request.user.id

        date = datetime.now()
        
        x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forw_for is not None:
            ip = x_forw_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        

        data = Banners (Date=date,AddedBy=user,Ip=ip,Caption=caption,Sub_Caption=scaption,Button_Label=label,Link=link,Banner_Image=image)
        data.save()
        messages.success(request,'banner added')
        return redirect('banner')
    
    context = {
        'manage' : manage
    }

    return render(request,'banner.html',context)

########################################################################

@login_required
def manage_banner(request):
    manage = Manage_Menu.objects.last()
    banners = Banners.objects.filter(Status=1)
    context = {
        'banners' : banners,
        'manage' : manage
    }
    return render(request,'manage_banner.html',context)

########################################################################

@login_required
def edit_banner(request,bid):
    manage = Manage_Menu.objects.last()
    banner = Banners.objects.get(id=bid)

    user = request.user.id
        
    x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forw_for is not None:
        ip = x_forw_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    if request.method == 'POST':
        if len(request.FILES) != 0:
        #     if len(banner.Banner_Image) > 0:
        #         os.remove(banner.Banner_Image.path)
            banner.Banner_Image = request.FILES['image']
        banner.Caption = request.POST.get('caption')
        banner.Sub_Caption = request.POST.get('scaption')
        banner.Button_Label = request.POST.get('label')
        banner.Link = request.POST.get('link')
        banner.EditedBy = user
        banner.EditedIp = ip
        banner.Edited_Date = datetime.now()
        banner.save()
        messages.success(request,'banner edited')
        return redirect('.')
    context = {
        'banner' : banner,
        'manage' : manage,
    }
    return render(request,'edit_banner.html',context)

########################################################################

@login_required
def remove_banner(request,bid):
    banner = Banners.objects.get(id=bid)

    banner.Status = 0
    banner.save()
    messages.success(request,'banner deleted')
    return redirect('manage_banner')

########################################################################

@login_required
def remove_ban_img(request,bid):
    banner = Banners.objects.get(id=bid)

    banner.Banner_Image.delete(save=True)
    banner.save()

    return redirect('/admin/edit_banner/%s' %banner.id)