from django.shortcuts import render
from publicapp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def mprofile(request):
    id=request.session['motherid']
    prof=tbl_reg.objects.get(id=id)       
    return render(request,"motherapp/mprofile.html",{'prof':prof})

def edit_mprofile(request):
    id=request.session['motherid']
    data=tbl_reg.objects.get(id=id)
    item=tbl_log.objects.get(username=data.email)
    if request.method=="POST":
        a=request.POST.get('r1')
        b=request.POST.get('r2')
        c=request.POST.get('r3')
        d=request.POST.get('r4')
        e=request.POST.get('r5')
        f=request.POST.get('r6')
        g=request.POST.get('r7')
        h=request.POST.get('r8')
        i=request.POST.get('r9')
        j=request.POST.get('r10')
        k=request.POST.get('r11')

        data.mother_name=a
        data.mother_age=b
        data.mother_bloodgroup=c
        data.baby_name=d
        data.baby_age=e
        data.baby_bloodgroup=f
        data.email=g
        data.number=h
        data.anganvadi=i
        data.place=j
        item.username=g
        item.password=k
        data.save()
        item.save()
        return HttpResponseRedirect(reverse('mprofile'))     
    return render(request,"motherapp/edit_mprofile.html",{'data':data,'item':item})

def mdoctors(request):
    id=request.session['motherid']
    data=tbl_doctor.objects.all()
    return render(request,"motherapp/mdoctors.html",{'data':data})

def msgd(request,id):
    m_id=request.session['motherid']
    mid=tbl_reg.objects.get(id=m_id)
    did=tbl_doctor.objects.get(id=id)
    msg=''
    if request.method=="POST":
        msg=request.POST.get('c1')
        a=m_id
        b=mid.mother_name
        c=did.usertype
        d=id
        e=msg
        data=tbl_mothermsg.objects.create(mother_id=a,mother_name=b,re=c,re_id=d,message=e)
        msg='Your message sent successfully'
    return render(request,"motherapp/msgd.html",{'msg':msg,'did':did})

def mworkers(request):
    data=tbl_worker.objects.all()
    return render(request,"motherapp/mworkers.html",{'data':data})

def msgw(request,id):
    m_id=request.session['motherid']
    mid=tbl_reg.objects.get(id=m_id)
    did=tbl_worker.objects.get(id=id)
    msg=''
    if request.method=="POST":
        msg=request.POST.get('c1')
        a=m_id
        b=mid.mother_name
        c=did.usertype
        d=id
        e=msg
        data=tbl_mothermsg.objects.create(mother_id=a,mother_name=b,re=c,re_id=d,message=e)
        msg='Your message sent successfully'    
    return render(request,"motherapp/msgw.html",{'msg':msg,'did':did})

def minbox(request):
    id=request.session['motherid']
    data=tbl_message.objects.filter(mother_id=id)
    return render(request,"motherapp/minbox.html",{'data':data})

def mcontact(request):
    id=request.session['motherid']
    prof=tbl_reg.objects.get(id=id)
    msg=''
    if request.method=="POST":
        a=prof.mother_name
        b=prof.email
        c=request.POST.get('r3')
        data=tbl_contact.objects.create(name=a,email=b,message=c,reply='REPLY',replymsg='nill',user='mother')
        msg='Your message sent successfully!!!'    
    return render(request,"motherapp/mcontact.html",{'prof':prof,'msg':msg})