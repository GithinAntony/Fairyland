"""Fairyland URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from publicapp.views import *
from adminapp.views import *
from doctorapp.views import *
from workerapp.views import *
from motherapp.views import *
from django.urls import re_path as url

urlpatterns = [
    path('admin/', admin.site.urls),
    #Public_Module
    url(r'^$',home,name="home"),
    url(r'^about/$',about,name="about"),
    url(r'^service/$',service,name="service"),
    url(r'^register/$',register,name="register"),
    url(r'^login/$',login,name="login"),
    url(r'^logout/$',logout,name='logout'),
    url(r'^contact/$',contact,name="contact"),

    #Admin_Module
    url(r'^view_users/$',view_users,name="view_users"),
    url(r'^approve/(?P<id>[0-9]+)',approve,name='approve'),
    url(r'^view_active_users/$',view_active_users,name="view_active_users"),
    url(r'^delete/(?P<id>[0-9]+)',delete,name='delete'),
    url(r'^add_doctors/$',add_doctors,name="add_doctors"),
    url(r'^view_doctors/$',view_doctors,name="view_doctors"),
    url(r'^doctor_delete/(?P<id>[0-9]+)',doctor_delete,name='doctor_delete'),
    url(r'^add_workers/$',add_workers,name="add_workers"),
    url(r'^view_workers/$',view_workers,name="view_workers"),
    url(r'^worker_delete/(?P<id>[0-9]+)',worker_delete,name='worker_delete'),
    url(r'^view_contact/$',view_contact,name="view_contact"),
    url(r'^reply/(?P<id>[0-9]+)',reply,name="reply"),

    #Doctor_Module
    url(r'^dprofile/$',dprofile,name="dprofile"),
    url(r'^edit_dprofile/$',edit_dprofile,name="edit_dprofile"),
    url(r'^dmothers/$',dmothers,name="dmothers"),
    url(r'^dmsg/(?P<id>[0-9]+)',dmsg,name="dmsg"),
    url(r'^dinbox/$',dinbox,name="dinbox"),
    url(r'^dcontact/$',dcontact,name="dcontact"),

    #Worker_Module
    url(r'^wprofile/$',wprofile,name="wprofile"),
    url(r'^edit_wprofile/$',edit_wprofile,name="edit_wprofile"),
    url(r'^wmothers/$',wmothers,name="wmothers"),
    url(r'^wmsg/(?P<id>[0-9]+)',wmsg,name="wmsg"),
    url(r'^winbox/$',winbox,name="winbox"),
    url(r'^wcontact/$',wcontact,name="wcontact"),

    #Mother_Module
    url(r'^mprofile/$',mprofile,name="mprofile"),
    url(r'^edit_mprofile/$',edit_mprofile,name="edit_mprofile"),
    url(r'^mdoctors/$',mdoctors,name="mdoctors"),
    url(r'^msgd/(?P<id>[0-9]+)',msgd,name="msgd"),
    url(r'^mworkers/$',mworkers,name="mworkers"),
    url(r'^msgw/(?P<id>[0-9]+)',msgw,name="msgw"),
    url(r'^minbox/$',minbox,name="minbox"),
    url(r'^mcontact/$',mcontact,name="mcontact"),


    ]
