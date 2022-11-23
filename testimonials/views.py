from django.shortcuts import render,redirect
from home.models import Testimonial,Manage_Menu
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
# Create your views here.

@login_required
def add_testimonial(request):
    manage = Manage_Menu.objects.last()
    if request.method == 'POST' :
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        cname = request.POST.get('cname')
        image = request.FILES['image']
        testimonial = request.POST.get('testimonial')

        user = request.user.id

        date = datetime.now()
        
        x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forw_for is not None:
            ip = x_forw_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        data = Testimonial(Date=date,AddedBy=user,Ip=ip,Tes_Name=name,Designation=designation,Company_Name=cname,Testimonial=testimonial,Tes_Image=image)
        data.save()
        messages.success(request,'testimonial added')
        return redirect('add_testimonial')

    context = {
        'manage' : manage
    }
    return render(request,'add_testimonial.html',context)

########################################################################

@login_required
def manage_testimonial(request):
    manage = Manage_Menu.objects.last()
    testimonials = Testimonial.objects.filter(Status = 1)
    context = {
        'testimonials' : testimonials,
        'manage' : manage,
    }
    return render(request,'manage_testimonial.html',context)

########################################################################

@login_required
def edit_testimonial(request,tid):
    testimonial = Testimonial.objects.get(id=tid)
    manage = Manage_Menu.objects.last()

    user = request.user.id
        
    x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forw_for is not None:
        ip = x_forw_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    if request.method == 'POST':
        if len(request.FILES) != 0:
        #     if len(testimonial.Image) > 0:
        #         os.remove(testimonial.Image.path)
            testimonial.Tes_Image = request.FILES['image']
        testimonial.EditedBy = user
        testimonial.EditedIp = ip
        testimonial.Edited_Date = datetime.now()
        testimonial.Tes_Name = request.POST.get('name')
        testimonial.Designation = request.POST.get('designation')
        testimonial.Company_Name = request.POST.get('cname')
        testimonial.Testimonial = request.POST.get('testimonial')
        testimonial.save()
        messages.success(request,'testimonial edited')
        return redirect('.')
    context = {
        'tes' : testimonial,
        'manage' : manage,
    }
    return render(request,'edit_testimonial.html',context)

########################################################################

@login_required
def remove_testimonial(request,tid):
    testimonial = Testimonial.objects.get(id=tid)

    testimonial.Status = 0
    testimonial.save()
    messages.success(request,'testimonial deleted')
    return redirect('manage_testimonial')

########################################################################

@login_required
def remove_tes_img(request,tid):
    testimonial = Testimonial.objects.get(id=tid)

    testimonial.Tes_Image.delete(save=True)
    testimonial.save()

    return redirect('/admin/edit_testimonial/%s' %testimonial.id)