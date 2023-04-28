from django.shortcuts import render,redirect
from . models import *
from doctor. models import *
from estimator. models import *
from lapapp. models import *
from patient. models import *
from django.db import IntegrityError
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def admin_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email)
        if email == "admin@gmail.com" and password == "admin":
            print(email)
            request.session['admin'] = "admin@gmail.com"
            messages.info(request, "Successfully Login ")
            return render(request,'admin/home_admin.html')
        elif email != "admin@gmail.com":
            messages.error(request, "Wrong Mail id")
            return render (request,'admin/admin_login.html')
        elif password != "admin":
            messages.error(request,"wrong password")
            return render (request, 'admin/admin_login.html')
        else:
            return render(request,'admin/admin_login.html')
    return render(request,'admin/admin_login.html')


def admin_logout(request):
    if 'admin' in request.session:
        request.session.pop('admin',None)
        messages.success(request,'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/admin_logout/')


def admin_home(request):
    return render(request, 'admin/home_admin.html')


def approve_patient_details(request):
    if 'admin' in request.session:
        values = patientRegister.objects.filter(admin_approve=False)
        return render(request,'admin/approve_patients.html',{'values': values})


def approve_patient_true(request,id):
    if "admin" in request.session:
        print('hi')
        values = patientRegister.objects.get(id=id)
        values.admin_approve= True
        values.save()
        print('hi')
        messages.info(request, "successfully approved")
        return redirect('/approve_patient_details/')


def approve_doctor_details(request):
    if 'admin' in request.session:
        values = doctorRegister.objects.filter(admin_approve=False)
        return render(request,'admin/approve_doctor.html',{'values': values})


def approve_doctor_true(request,id):
    if "admin" in request.session:
        print('hi')
        values = doctorRegister.objects.get(id=id)
        values.admin_approve = True
        values.save()
        print('hi')
        messages.info(request, "successfully approved")
        return redirect('/approve_doctor_details/')


def approve_estimator_details(request):
    if 'admin' in request.session:
        values = estimatorRegister.objects.filter(approve_estimator=False)
        return render(request,'admin/approve_estimator.html',{'values': values})


def approve_estimator_true(request,id):
    if "admin" in request.session:
        print('hi')
        values = estimatorRegister.objects.get(id=id)
        values.approve_estimator = True
        values.save()
        print('hi')
        messages.info(request, "successfully approved")
        return redirect('/approve_estimator_details/')


def approve_lab_test_details(request):
    if 'admin' in request.session:
        values = lapRegister.objects.filter(approve_lab=False)
        return render(request,'admin/approve_lab_test.html',{'values': values})


def approve_lab_test_true(request,id):
    if "admin" in request.session:
        print('hi')
        values = lapRegister.objects.get(id=id)
        values.approve_lab = True
        values.save()
        print('hi')
        messages.info(request, "successfully approved")
        return redirect('/approve_lab_test_details/')

