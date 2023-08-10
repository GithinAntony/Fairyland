from django.shortcuts import render
from publicapp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def wprofile(request):
    id=request.session['workerid']
    prof=tbl_worker.objects.get(id=id)      
    return render(request,"workerapp/wprofile.html",{'prof':prof})

def edit_wprofile(request):
    id=request.session['workerid']
    data=tbl_worker.objects.get(id=id)
    item=tbl_log.objects.get(username=data.email)
    if request.method=="POST":
        a=request.POST.get('r1')
        b=request.POST.get('r2')
        c=request.POST.get('r3')
        d=request.POST.get('r4')
        e=request.POST.get('r5')
        f=request.POST.get('r6')
        g=request.POST.get('r7')
        data.name=a
        data.worker_id_number=b
        data.email=c
        data.number=d
        data.address=e
        data.place=f
        item.username=c
        item.password=g
        data.save()
        item.save()
        return HttpResponseRedirect(reverse('wprofile'))        
    return render(request,"workerapp/edit_wprofile.html",{'data':data,'item':item})

def wmothers(request):
    id=request.session['workerid']
    data=tbl_reg.objects.filter(approve='APPROVED!!!')    
    return render(request,"workerapp/wmothers.html",{'data':data})

def wmsg(request,id):
    d_id=request.session['workerid']
    did=tbl_worker.objects.get(id=d_id)
    mid=tbl_reg.objects.get(id=id)
    msg=''
    if request.method=="POST":
        msg=request.POST.get('c1')
        a=did.usertype
        b=d_id
        c=id
        d=msg
        data=tbl_message.objects.create(sender=a,sid=b,mother_id=c,message=d)
        msg='Your message sent successfully'
    return render(request,"workerapp/wmsg.html",{'mid':mid,'msg':msg})

def winbox(request):
    id=request.session['workerid']
    data=tbl_mothermsg.objects.filter(re_id=id)
    return render(request,"workerapp/winbox.html",{'data':data})

def wcontact(request):
    id=request.session['workerid']
    prof=tbl_worker.objects.get(id=id)
    msg=''
    if request.method=="POST":
        a=prof.name
        b=prof.email
        c=request.POST.get('r3')
        data=tbl_contact.objects.create(name=a,email=b,message=c,reply='REPLY',replymsg='nill',user='worker')
        msg='Your message sent successfully!!!'
    return render(request,"workerapp/wcontact.html",{'msg':msg,'prof':prof})
