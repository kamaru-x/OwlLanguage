from django.shortcuts import render,redirect
from home.models import Group_Of_Companies,Manage_Menu
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
# Create your views here.

@login_required
def add_logo(request):
    manage = Manage_Menu.objects.last()
    if request.method == 'POST' :
        image = request.FILES.getlist('image')

        user = request.user.id

        date = datetime.now()
        
        x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forw_for is not None:
            ip = x_forw_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        for img in image :
            data = Group_Of_Companies(Date=date,AddedBy=user,Ip=ip,Logo=img)
            data.save()
        messages.success(request,'logo added')
        return redirect('add_logo')

    context = {
        'manage' : manage
    }

    return render(request,'add_logo.html',context)

########################################################################

@login_required
def manage_logo(request):
    manage = Manage_Menu.objects.last()
    logos = Group_Of_Companies.objects.filter(Status = 1)
    context = {
        'logos' : logos,
        'manage' : manage,
    }
    return render(request,'manage_logo.html',context)

########################################################################

@login_required
def remove_logo(request,lid):
    logo = Group_Of_Companies.objects.get(id=lid)

    logo.Status = 0
    logo.save()
    messages.success(request,'logo deleted')
    return redirect('manage_logo')

########################################################################