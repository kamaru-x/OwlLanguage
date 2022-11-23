from django.shortcuts import render,redirect
from home.models import Album,Album_Image,Manage_Menu
from home.forms import AboutForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.

########################################################################

@login_required
def create_album(request):
    manage = Manage_Menu.objects.last()
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES['image']
        url = request.POST.get('url')
        smtitle = request.POST.get('smtitle')
        smkeywords = request.POST.get('smkeywords')
        smdescription = request.POST.get('smdescription')

        urls = Album.objects.all()

        for u in urls :
            if u.Url == url:
                messages.error(request,'album already exist with same name and url')
                return redirect('create_album')
            else:
                pass

        user = request.user.id

        date = datetime.now()
        
        x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forw_for is not None:
            ip = x_forw_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        
        Data = Album(Date=date,AddedBy=user,Ip=ip,Title=title,Thumbnail=image,Url=url,SMTitle=smtitle,
        SMDescription=smdescription,SMKeywords=smkeywords)
        Data.save()
        messages.success(request,'album created successfully...!')
        return redirect('create_album')

    context = {
        'manage' : manage
    }
    
    return render(request,'create_album.html',context)

########################################################################

@login_required
def view_ablum(request,aid):
    album = Album.objects.get(id=aid)
    manage = Manage_Menu.objects.last()
    context = {
        'album' : album,
        'manage' : manage,
    }
    return render(request,'album_view.html',context)

########################################################################

@login_required
def upload_image(request):
    manage = Manage_Menu.objects.last()
    albums = Album.objects.all()

    user = request.user.id

    date = datetime.now()
        
    x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forw_for is not None:
        ip = x_forw_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    if request.method == 'POST':
        select = request.POST.get('select')
        image = request.FILES.getlist('image')

        album = Album.objects.get(id=select)
        image_count = Album_Image.objects.filter(Album_Name=album).filter(Status=1).count()

        album.Images = image_count + len(image)
        album.save()

        for img in image: 
            Data = Album_Image(Date=date,AddedBy=user,Ip=ip,Album_Name=album,Image=img,)
            Data.save()
        messages.success(request,'image uploaded successfully ...!')
        return redirect('upload_image')
    context = {
        'albums' : albums,
        'manage' : manage,
    }
    return render(request,'upload_image.html',context)

########################################################################

@login_required
def manage_album(request):
    albums = Album.objects.filter(Status=1)
    manage = Manage_Menu.objects.last()
    context = {
        'albums' : albums,
        'manage' : manage,
    }
    return render(request,'manage_album.html',context)

########################################################################

@login_required
def edit_album(request,aid):
    album = Album.objects.get(id=aid)
    images_list = Album_Image.objects.filter(Album_Name=aid)
    manage = Manage_Menu.objects.last()

    images = []

    for img in images_list:
        if img.Status == 1 :
            images.append(img)


    user = request.user.id
        
    x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forw_for is not None:
        ip = x_forw_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    if request.method == 'POST' :
        if len(request.FILES) != 0:
        #         if len(album.Image) > 0:
        #             os.remove(album.Image.path)
            album.Thumbnail = request.FILES['image']
        album.Title = request.POST.get('name')
        album.EditedBy = user
        album.EditedIp = ip
        album.Edited_Date = datetime.now()
        album.save()
        messages.success(request,'album details edited successfully')
        return redirect('/admin/edit_album/%s' %album.id)
    context = {
        'album' : album,
        'images' : images,
        'manage' : manage,
    }
    return render(request,'edit_album.html',context)

########################################################################

@login_required
def remove(request,aid):
    album = Album.objects.get(id=aid)
    album.Status = 0
    album.save()
    messages.success(request,'album deleted successfully')
    return redirect('manage_album')

########################################################################

@login_required
def remove_image(request,aid,iid):
    album = Album.objects.get(id=aid) 
    image = Album_Image.objects.get(id=iid)
    image.Status = 0
    image.save()
    messages.success(request,'image deleted successfully')
    return redirect('/admin/edit_album/%s' %album.id)

########################################################################