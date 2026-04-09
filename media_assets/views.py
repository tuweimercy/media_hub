'''get_object_or_404: this is a inbuilt operation thar 
presents 404 page not found error if data that does not exist  is required'''
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages #alerts
'''to control content fetch i.e if database has a lot of records 
we fetch the records in batches'''
from django.core.paginator import Paginator
from django.db.models import Q #q :query : sending commands to the db
from .models import MediaAssets
from .forms import MediaAssetsForm
# Create your views here.

@login_required
def dashboard_view(request):
    '''main dashboard:show all public media assets'''
    #capture all assets from media assets db table that are public
    media_list=MediaAssets.object.filter(is_public=True)
    #get data from a form using the name attribute
    #this power a search functionality for my users to be able to
    #filter the media assets
    query= request.GET.get('q')
    if query:
        media_list=media_list.filter(
            Q(title__icontains=query)/
            Q(description__icontains=query)
        )
        Paginator=Paginator(media_list,12)
        page_number=request.GET.get('page')
        media_asets=Paginator.get_page(page_number)
        
    return render(request,'media_assets/dashboard.html',
    {
        'media_assets':media_asets,
        'query': query
    })
##view to showcase only media files belonging to the logged in user
@login_required
def my_media_view(request):
    '''user own media assets'''
    media_list =MediaAssets.object.filter(uploaded_by=request.user)
    #pagination
    Paginator=Paginator(media_list,12)
    page_number=request.GET.get('page')
    media_assets =Paginator.get_page(page_number)
    return render(request,'media_assets/my_media.html',{
        'media_assets':media_assets
    })

##upload view(create /post a media asset to our db)
@login_required
def upload_view(request):
    if request.method == "POST":
        form=MediaAssetsForm(request.POST,request.FILES)
        if form.valid():
            media= form.save(commit=False)#delay post
            media.uploaded_by = request.user#tagging user to post
            media.save()
            messages.success(request,'Media Uploaded Succefully!')
            return redirect('media_assets::my_media')
    else:
        form=MediaAssetsForm()
    return render(request,'media_assets/upload_media.html',{
        'form':form
    })    

##view to control full media details
# view to be also be used in updating the view count
@login_required
def media_detail_view(request,pk):
    '''pk:primary key (uniquely identifies a record ib
    a db table):we use this to identify the
    role of current user'''
    '''showcase the full details of a media assets''' 
    #get_object_or_404 to handle the data fetch
    # i.e if object exists tag it if not showcase a 404 page.
    media= get_object_or_404(MediaAssets,pk=pk) 
    #app specification #tag on whether media is private or not
    if not media.is_public and media_uploaded_by !=request.user and not request.user.is_teacher() and not request.is_superuser:
        messages.error(request,"This media is private!!")
        return redirect('media_assets:dashboard')
    ## if user is a teacher ,superuser or the media is public
    # increment the view count
    media.views_count += 1 # updating the medias vieew count
    media.save(update_fields=['views_count'])
    # compare edit and delete permissions for the media
    can_edit =media.can_edit(request.user)
    can_delete=media.can_delete(request.user)
    return render(request, 'media_assets/media_detail.html',{
        'media':media,
        'can_edit':can_edit,
        'can_delete':can_delete,
    })
# edit and deleting views
def edit_media_view(request,pk):
    '''only allow editing if user is the person who uploaded 
    media or superuser/teacher'''
    media=get_object_or_404(MediaAssets,pk=pk)
    if not media.can_edit(request.user):
        messages.error(request,"You cannot edit this file")
        return redirect('media_assets:dashboard')
    if request.method == 'POST':
        form = MediaAssetsForm(request.POST,request.FILES,
        instance=media)
        if form.valid():
            form.save()
            messages.success(request,"Media Asset Updated")
            return redirect("media_assets:media_detail",pk=pk)
    else :
        form=MediaAssetsForm(instance=media)
    return render(request, 'media_assets/edit_media.html',{
        'form':form,
        'media':media,
    })
@login_required
def delete_media_view(request,pk):
    '''delete media assets based off pk'''
    if not media.can_delete(request.user):
        messages.error(request,"You cannot delete media")
        return redirect('media_assets:dashboard')
    if request.method == 'PPOST':
        media.delete()#delete from db
        messages.success(request,"Deleted Successfully")
        return redirect('media_assets:my_media')
    return render(request,'media_assets:delete_media.html',{
        'media':media
    })
