from django.db import models

# Create your models here.

class tbl_log(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    usertype=models.CharField(max_length=50)

class tbl_reg(models.Model):
    mother_name=models.CharField(max_length=100)
    mother_bloodgroup=models.CharField(max_length=50)
    baby_name=models.CharField(max_length=100)
    baby_bloodgroup=models.CharField(max_length=50)
    mother_age=models.CharField(max_length=50)
    anganvadi=models.CharField(max_length=100)
    baby_age=models.CharField(max_length=50)
    place=models.CharField(max_length=100)
    number=models.CharField(max_length=50,default='0000000000')
    email=models.CharField(max_length=100,default='user@email.com')
    place=models.CharField(max_length=100)
    approve=models.CharField(max_length=50)
    usertype=models.CharField(max_length=50)

class tbl_doctor(models.Model):
    name=models.CharField(max_length=100)
    licence_number=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    number=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    hospital=models.CharField(max_length=100)
    usertype=models.CharField(max_length=50)

class tbl_worker(models.Model):
    name=models.CharField(max_length=100)
    worker_id_number=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    number=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    place=models.CharField(max_length=50)
    usertype=models.CharField(max_length=50)

class tbl_contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    message=models.CharField(max_length=10000)
    reply=models.CharField(max_length=50)
    replymsg=models.CharField(max_length=10000)
    user=models.CharField(max_length=100,default='public')

class tbl_message(models.Model):
    sender=models.CharField(max_length=100)
    sid=models.CharField(max_length=50)
    mother_id=models.CharField(max_length=50)
    message=models.CharField(max_length=10000)

class tbl_mothermsg(models.Model):
    mother_id=models.CharField(max_length=100)
    mother_name=models.CharField(max_length=100,default='user')
    re=models.CharField(max_length=50)
    re_id=models.CharField(max_length=50)
    message=models.CharField(max_length=10000)
