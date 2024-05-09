from django.shortcuts import render,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import *

def home(Request):
    spdata = Speeche.objects.all().order_by("id").reverse()[:6] 
    nwdata = News.objects.all().order_by("id").reverse()[:2]
    dudata = DailyUpdate.objects.all().order_by("id").reverse()[:4]
    sbdata = SliderBanner.objects.all()
    olpdata = OnLoadPopup.objects.get()
    return render(Request,"index.html",{"nwdata":nwdata,"dudata":dudata,"spdata":spdata,"olpdata":olpdata,"sbdata":sbdata})

def biography(Request):
    return render(Request,"biography.html")

def journey(Request):
    return render(Request,"journey.html")

def achievements(Request):
    return render(Request,"achievements.html")

def speeches(Request):
    totalPagelist = [] 
    page_range = []
    
    if(Request.method=="POST"):
        search = Request.POST.get("date")
        spdatafinal = Speeche.objects.filter(date__icontains=search)
    else:


        spdata = Speeche.objects.all().order_by("id").reverse() 
        paginator = Paginator(spdata,9)

        page_number = Request.GET.get('page')
        spdatafinal = paginator.get_page(page_number)
        total_pages = spdatafinal.paginator.num_pages
        totalPagelist = [n+1 for n in range(total_pages)]
        current_page = spdatafinal.number
        page_range = range(max( current_page - 2 if current_page == total_pages else current_page - 1, 1), min(current_page + 3 if current_page == 1 else current_page + 2, total_pages + 1))
    return render(Request,"speeches.html",{"spdatafinal":spdatafinal,"totalPagelist":totalPagelist,"page_range":page_range})

def speechesDetails(Request,id):
    spddata = Speeche.objects.get(id=id)
    return render(Request,"speeches-details.html",{"spddata":spddata})

def videos(Request):
    ytvdata = YouTubeVideo.objects.all().order_by("id").reverse()
    paginator = Paginator(ytvdata,6)

    page_number = Request.GET.get('page')
    ytvdatafinal = paginator.get_page(page_number)
    total_pages = ytvdatafinal.paginator.num_pages
    totalPagelist = [n+1 for n in range(total_pages)]
    current_page = ytvdatafinal.number
    page_range = range(max( current_page - 2 if current_page == total_pages else current_page - 1, 1), min(current_page + 3 if current_page == 1 else current_page + 2, total_pages + 1))
    return render(Request,"videos.html",{"ytvdatafinal":ytvdatafinal,"total_pages":total_pages,"totalPagelist":totalPagelist,"page_range":page_range})

def mediaCoverage(Request):
    mcdata = MediaCoverage.objects.all().order_by("id").reverse()
    paginator = Paginator(mcdata,5)

    page_number = Request.GET.get('page')
    mcdatafinal = paginator.get_page(page_number)
    total_pages = mcdatafinal.paginator.num_pages
    totalPagelist = [n+1 for n in range(total_pages)]
    current_page = mcdatafinal.number
    page_range = range(max( current_page - 2 if current_page == total_pages else current_page - 1, 1), min(current_page + 3 if current_page == 1 else current_page + 2, total_pages + 1))
    return render(Request,"media-coverage.html",{"mcdatafinal":mcdatafinal,"totalPagelist":totalPagelist,"page_range":page_range})

def mediaCoverageDetails(Request,id):
    mcddata = MediaCoverage.objects.get(id=id)
    return render(Request,"media-coverage-details.html",{"mcddata":mcddata})

def news(Request):
    nwdata = News.objects.all().order_by("id").reverse()
    paginator = Paginator(nwdata,5)

    page_number = Request.GET.get('page')
    nwdatafinal = paginator.get_page(page_number)
    total_pages = nwdatafinal.paginator.num_pages
    totalPagelist = [n+1 for n in range(total_pages)]
    current_page = nwdatafinal.number
    page_range = range(max( current_page - 2 if current_page == total_pages else current_page - 1, 1), min(current_page + 3 if current_page == 1 else current_page + 2, total_pages + 1))
    return render(Request,"news.html",{"nwdata":nwdata,"nwdatafinal":nwdatafinal,"totalPagelist":totalPagelist,"page_range":page_range})

def newsDetails(Request,id):
    nwddata = News.objects.get(id=id)
    return render(Request,"news-details.html",{"nwddata":nwddata})

def gallery(Request):
    gldata = Gallery.objects.all().order_by("id").reverse()
    paginator = Paginator(gldata,9)

    page_number = Request.GET.get('page')
    gldatafinal = paginator.get_page(page_number)
    total_pages = gldatafinal.paginator.num_pages
    totalPagelist = [n+1 for n in range(total_pages)]
    current_page = gldatafinal.number
    page_range = range(max( current_page - 2 if current_page == total_pages else current_page - 1, 1), min(current_page + 3 if current_page == 1 else current_page + 2, total_pages + 1))
    return render(Request,"gallery.html",{"gldatafinal":gldatafinal,"totalPagelist":totalPagelist,"page_range":page_range})

def videosGallery(Request):
    vgdata = VideosGallery.objects.all().order_by("id").reverse()
    paginator = Paginator(vgdata,5)

    page_number = Request.GET.get('page')
    vgdatafinal = paginator.get_page(page_number)
    total_pages = vgdatafinal.paginator.num_pages
    totalPagelist = [n+1 for n in range(total_pages)]
    current_page = vgdatafinal.number
    page_range = range(max( current_page - 2 if current_page == total_pages else current_page - 1, 1), min(current_page + 3 if current_page == 1 else current_page + 2, total_pages + 1))
    return render(Request,"videos-gallery.html",{"vgdatafinal":vgdatafinal,"totalPagelist":totalPagelist,"page_range":page_range})

def videosGalleryDetails(Request,id):
    vgddata = VideosGallery.objects.get(id=id)
    return render(Request,"videos-gallery-details.html",{"vgddata":vgddata})

def dailyUpdates(Request):
    dudata = DailyUpdate.objects.all().order_by("id").reverse()
    paginator = Paginator(dudata,5)

    page_number = Request.GET.get('page')
    dudatafinal = paginator.get_page(page_number)
    total_pages = dudatafinal.paginator.num_pages
    totalPagelist = [n+1 for n in range(total_pages)]
    current_page = dudatafinal.number
    page_range = range(max( current_page - 2 if current_page == total_pages else current_page - 1, 1), min(current_page + 3 if current_page == 1 else current_page + 2, total_pages + 1))
    return render(Request,"daily-updates.html",{"dudata":dudata,"dudatafinal":dudatafinal,"totalPagelist":totalPagelist,"page_range":page_range})

def dailyUpdatesDetails(Request,id):
    duddata = DailyUpdate.objects.get(id=id)
    return render(Request,"daily-updates-details.html",{"duddata":duddata}) 

def contact(Request):
    if(Request.method=="POST"):
        cd = ContactDetail()
        cd.name = Request.POST.get("username")
        cd.email = Request.POST.get("email")
        cd.contact = Request.POST.get("phone")
        cd.address = Request.POST.get("address")
        cd.message = Request.POST.get("message")
        cd.save()
        messages.success(Request,"Message Sent Successfully !!!")
    return render(Request,"contact.html")

def businessQuery(Request):
    if(Request.method=="POST"):
        bqd = BusinessQueryDetail()
        bqd.name = Request.POST.get("name")
        bqd.businessName = Request.POST.get("business")
        bqd.email = Request.POST.get("email")
        bqd.contact = Request.POST.get("phone")
        bqd.address = Request.POST.get("address")
        bqd.location = Request.POST.get("location")
        bqd.query = Request.POST.get("query")
        bqd.save()
        messages.success(Request,"Your Query/Complaints Sent Successfully !!!")
    return render(Request,"business-query.html")

def newsletterSubscription(Request):
    if(Request.method=="POST"):
        ns = NewsletterSubscription()
        ns.email = Request.POST.get("email")
        if(NewsletterSubscription.objects.filter(email=ns.email)):
            messages.success(Request,"Already Subscribed !!!")
        else:
            ns.save()
            messages.success(Request,"Thankyou For Your Subscription !!!")
    return redirect("/")

