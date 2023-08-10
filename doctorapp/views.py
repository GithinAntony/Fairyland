from django.shortcuts import render
from publicapp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def dprofile(request):
    id=request.session['doctorid']
    prof=tbl_doctor.objects.get(id=id)    
    return render(request,"doctorapp/dprofile.html",{'prof':prof})

def edit_dprofile(request):
    id=request.session['doctorid']
    data=tbl_doctor.objects.get(id=id)
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
        data.licence_number=b
        data.email=c
        data.number=d
        data.address=e
        data.hospital=f
        item.username=c
        item.password=g
        data.save()
        item.save()
        return HttpResponseRedirect(reverse('dprofile'))    
    return render(request,"doctorapp/edit_dprofile.html",{'data':data,'item':item})

def dmothers(request):
    id=request.session['doctorid']
    data=tbl_reg.objects.filter(approve='APPROVED!!!')
    return render(request,"doctorapp/dmothers.html",{'data':data})

def dmsg(request,id):
    d_id=request.session['doctorid']
    did=tbl_doctor.objects.get(id=d_id)
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
    return render(request,"doctorapp/dmsg.html",{'mid':mid,'msg':msg})

def dinbox(request):
    id=request.session['doctorid']
    data=tbl_mothermsg.objects.filter(re_id=id)
    return render(request,"doctorapp/dinbox.html",{'data':data})

def dcontact(request):
    id=request.session['doctorid']
    prof=tbl_doctor.objects.get(id=id)
    msg=''
    if request.method=="POST":
        a=prof.name
        b=prof.email
        c=request.POST.get('r3')
        data=tbl_contact.objects.create(name=a,email=b,message=c,reply='REPLY',replymsg='nill',user='doctor')
        msg='Your message sent successfully!!!'
    return render(request,"doctorapp/dcontact.html",{'msg':msg,'prof':prof})
