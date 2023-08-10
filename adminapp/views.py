from django.shortcuts import render
from publicapp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def view_users(request):
    data=tbl_reg.objects.all()
    return render(request,"adminapp/view_users.html",{'data':data})

def approve(request,id):
    aprv=tbl_reg.objects.get(id=id)
    if aprv.approve=="APPROVE":
        password = User.objects.make_random_password(length=5, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889") # zvk0hawf8m6394
        new=tbl_log.objects.create(username=aprv.email,password=password,usertype=aprv.usertype)
        subject='Fairyland - Username & Password'
        message= "Hello "+aprv.mother_name+",\n this message is from Fairyland-Babycare.Your username is " + new.username + " and password is " + new.password + ".\n Thank you."
        email_from = settings.EMAIL_HOST_USER
        recipient_list=[aprv.email,]
        send_mail(subject,message,email_from,recipient_list,fail_silently=True)
        aprv.approve="APPROVED!!!"
        aprv.save()
    return HttpResponseRedirect(reverse('view_users'))

def view_active_users(request):
    data=tbl_log.objects.filter(usertype='mother')
    return render(request,"adminapp/view_active_users.html",{'data':data})

def delete(request,id):
    dele=tbl_reg.objects.filter(id=id).delete()
    data=tbl_reg.objects.all()
    return HttpResponseRedirect(reverse('view_active_users'))

def add_doctors(request):
    msg=""
    data=tbl_doctor.objects.all()
    if request.method=="POST":
        a=request.POST.get('r1')
        b=request.POST.get('r2')
        c=request.POST.get('r3')
        d=request.POST.get('r4')
        e=request.POST.get('r5')
        f=request.POST.get('r6')
        if tbl_doctor.objects.filter(email=c):
            msg="You added this doctor because this Username(Email ID) is already exists..."        
        else:
            data=tbl_doctor.objects.create(name=a,licence_number=b,email=c,number=d,address=e,hospital=f,usertype='doctor')
            password = User.objects.make_random_password(length=5, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889")
            subject='Fairyland - Username & Password'
            message= "Hello Dr."+ a +",\nthis message is from Fairyland-Babycare.Your username is " + c  + " and password is " + password + ".\nThank you."
            email_from = settings.EMAIL_HOST_USER
            recipient_list=[c,]
            send_mail(subject,message,email_from,recipient_list,fail_silently=True)
            data1=tbl_log.objects.create(username=c,password=password,usertype='doctor')
            msg='Doctor added successfully. Thank you!!!'
    return render(request,"adminapp/add_doctors.html",{'msg':msg})

def view_doctors(request):
    data=tbl_doctor.objects.all()
    return render(request,"adminapp/view_doctors.html",{'data':data})

def doctor_delete(request,id):
    dele=tbl_doctor.objects.filter(id=id).delete()
    data=tbl_doctor.objects.all()
    return HttpResponseRedirect(reverse('view_doctors'))

def add_workers(request):
    msg=""
    data=tbl_worker.objects.all()
    if request.method=="POST":
        a=request.POST.get('r1')
        b=request.POST.get('r2')
        c=request.POST.get('r3')
        d=request.POST.get('r4')
        e=request.POST.get('r5')
        f=request.POST.get('r6')
        if tbl_worker.objects.filter(email=c):
            msg="You added this worker because this Username(Email ID) is already exists..."        
        else:
            data=tbl_worker.objects.create(name=a,worker_id_number=b,email=c,number=d,address=e,place=f,usertype='worker')
            password = User.objects.make_random_password(length=5, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889")
            subject='Fairyland - Username & Password'
            message= "Hello "+ a +",\nthis message is from Fairyland-Babycare.Your username is " + c  + " and password is " + password + ".\nThank you."
            email_from = settings.EMAIL_HOST_USER
            recipient_list=[c,]
            send_mail(subject,message,email_from,recipient_list,fail_silently=True)
            data1=tbl_log.objects.create(username=c,password=password,usertype='worker')
            msg='Worker added successfully. Thank you!!!'
    return render(request,"adminapp/add_workers.html",{'msg':msg})

def view_workers(request):
    data=tbl_worker.objects.all()
    return render(request,"adminapp/view_workers.html",{'data':data})

def worker_delete(request,id):
    dele=tbl_worker.objects.filter(id=id).delete()
    data=tbl_worker.objects.all()
    return HttpResponseRedirect(reverse('view_workers'))

def view_contact(request):
    data=tbl_contact.objects.all()
    return render(request,"adminapp/view_contact.html",{'data':data})

def reply(request,id):
    re=tbl_contact.objects.get(id=id)
    if request.method=="POST":
        if re.reply=="REPLY":
            msg=request.POST.get('c1')
            name=re.name
            subject='Fairyland - Reply'
            message='Hi '+ name +' ,\nThis reply is from Fairyland.\n  '+ msg +'\nThank you, \nFairyland'
            email_from = settings.EMAIL_HOST_USER
            recipient_list=[re.email,]
            send_mail(subject,message,email_from,recipient_list,fail_silently=True)            
            re.reply="REPLIED!!!"
            re.replymsg=msg
            re.save()
        return HttpResponseRedirect(reverse('view_contact'))
    return render(request,"adminapp/reply.html",{'re':re})

