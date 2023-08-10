from django.shortcuts import render
from publicapp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request,"publicapp/home.html",{})

def about(request):
    return render(request,"publicapp/about.html",{})

def service(request):
    return render(request,"publicapp/service.html",{})

def register(request):
    msg=""
    data=tbl_reg.objects.all()
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
        if tbl_reg.objects.filter(email=j):
            msg="This Username(Email ID) is already taken. Please choose another..."
        else:        
            data=tbl_reg.objects.create(mother_name=a,mother_bloodgroup=b,baby_name=c,baby_bloodgroup=d,mother_age=e,anganvadi=f,baby_age=g,place=h,number=i,email=j,usertype='mother',approve='APPROVE')
            msg='Your registration done successfully. You will get your login details once admin approved your registration. Thank you!!!'
    return render(request,"publicapp/register.html",{'msg':msg})

def login(request):
    msg=''
    if request.method=="POST":
        a=request.POST.get('r1')
        b=request.POST.get('r2')
        if tbl_log.objects.filter(username=a,password=b):
            data=tbl_log.objects.get(username=a,password=b)
            
            usertype=data.usertype
            if usertype=="admin":
                request.session["adminid"]=data.id
                return HttpResponseRedirect(reverse('view_users')) 
            elif usertype=="doctor":
                data2=tbl_doctor.objects.get(email=a)
                request.session["doctorid"]=data2.id
                return HttpResponseRedirect(reverse('dprofile'))
            elif usertype=="worker":
                data2=tbl_worker.objects.get(email=a)
                request.session["workerid"]=data2.id
                return HttpResponseRedirect(reverse('wprofile'))
            elif usertype=="mother":
                data2=tbl_reg.objects.get(email=a)
                request.session["motherid"]=data2.id
                return HttpResponseRedirect(reverse('mprofile')) 
            else:
                msg='Invalid entry!!!'
        else:
            msg='Invalid username or password!!!'                               
    return render(request,"publicapp/login.html",{'msg':msg})

def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('home'))

def contact(request):
    msg=''
    if request.method=="POST":
        a=request.POST.get('r1')
        b=request.POST.get('r2')
        c=request.POST.get('r3')
        data=tbl_contact.objects.create(name=a,email=b,message=c,reply='REPLY',replymsg='nill',user='public')
        msg='Your message sent successfully!!!'
    return render(request,"publicapp/contact.html",{'msg':msg})