from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def topic(request):
    if request.method=='POST':
        to=request.POST['topic']
        TO=Topic.objects.get_or_create(topic_name=to)[0]
        TO.save()
        return HttpResponse('data is sumitted')

    return render(request,'topic.html')
def webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        topic=request.POST['tn']
        name=request.POST['name']
        url=request.POST['url']
        TO=Topic.objects.get(topic_name=topic)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WO.save()
        return HttpResponse('webpage insertion is done')
    return render(request,'webpage.html',d)
def accessrecord(request):
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    if request.method=='POST':
        name=request.POST['name']
        NO=Webpage.objects.get(name=name)
        
        date=request.POST['date']
        author=request.POST['author']
        AO=AccessRecord.objects.get_or_create(name=NO,date=date,author=author)[0]
        AO.save()
        return HttpResponse('Accessrecord is inserted')
    return render(request,'accessrecord.html',d)
def display_webpages(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        MST=request.POST.getlist('topic')#to get the selected options
        EWO=Webpage.objects.none()# to create one empty list
        for i in MST:
            EWO=EWO|Webpage.objects.filter(topic_name=i)
        d1={'EWO':EWO}
        return render(request,'display_webpages.html',d1)
    return render(request,'retrieve_webpage.html',d)
def display_accessrecords(request):
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    if request.method=='POST':
        MST=request.POST.getlist('name')#to get the selected options
        EAO=AccessRecord.objects.none()# to create one empty list
        for i in MST:
            EAO=EAO|AccessRecord.objects.filter(name=i)
        d1={'EAO':EAO}
        return render(request,'display_accessrecords.html',d1)
    return render(request,'retrieve_accessrecords.html',d)
def checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'checkbox.html',d)
