from django.shortcuts import render, redirect
from . models import *
from django.db import IntegrityError
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from patient.models import *
import random
from math import ceil
from decimal import Decimal
from lapapp.models import *


def lab_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            r = lapRegister.objects.get(email=email, password=password)
            request.session['lab'] = r.email
            print(request.session['lab'])
            if r is not None:
                messages.info(request, 'welcome')
                return redirect('/lab_home/')
        except lapRegister.DoesNotExist as e:
            messages.info(request, 'name does not exists')
            return redirect('/lab_login/')

    else:
        return render(request, 'lab_test/login.html')


def lab_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phoneno = request.POST['phoneno']
        Dateofbirth = request.POST['Dateofbirth']
        Address = request.POST['Address']
        password = request.POST['password']
        try:
            lapRegister(username=username, email=email, phoneno=phoneno, Dateofbirth=Dateofbirth, Address=Address,
                   password=password).save()
            messages.info(request, "successfully created")
            return redirect('/lab_login')
        except IntegrityError as e:
            messages.info(request, "name already exists")
            return redirect('/lab_register/')
    return render(request, 'lab_test/register.html')


def lab_home(request):
    return render(request,'lab_test/home_lab.html')


def lab_patient_basic_medical_details(request):
    basic_data = patient_detail.objects.filter(send_basic_lab=True)
    medical_data = patient_medical_details.objects.filter(send_medi_lab=True)
    return render (request, 'lab_test/patient_details.html',{'basic_data':basic_data,'medical_data':medical_data})


def lab_details(request):
    basic = patientRegister.objects.filter(admin_approve=True)
    return render(request,'lab_test/labtest.html',{'basic':basic})


def lab_test_patient(request):
    basic = patientRegister.objects.filter(admin_approve=True,second_approve=False)
    if request.method == 'POST':
        email = request.POST['email']
        contact_no = request.POST['contact_no']
        name = request.POST['name']
        Genes_in_mothers_side = request.POST['Genes_in_mothers_side']
        Blood_test_result = request.POST['Blood_test_result']
        Inherited_from_father = request.POST['Inherited_from_father']
        Maternal_gene = request.POST['Maternal_gene']
        Paternal_gene = request.POST['Paternal_gene']
        Gender = request.POST['Gender']
        Birth_defects = request.POST['Birth_defects']
        WhiteBlood_cell_count = request.POST['WhiteBlood_cell_count']
        test_date = request.POST['test_date']
        lab_test(contact_no=contact_no,name=name,Genes_in_mothers_side=Genes_in_mothers_side,
                 email=email,Blood_test_result=Blood_test_result,Inherited_from_father=Inherited_from_father,
                 Maternal_gene=Maternal_gene, Paternal_gene=Paternal_gene,Gender=Gender,
                 Birth_defects=Birth_defects,WhiteBlood_cell_count=WhiteBlood_cell_count,test_date=test_date).save()
    return render(request, 'lab_test/labtest.html', {'basic':basic})


def view_lab_test(request):
    data = lab_test.objects.filter(send_doctor_lab_report=False)
    return render(request,'lab_test/view_lab_test.html',{'data':data})


def send_to_doctor_labtest(request,id):
    if "lab" in request.session:
        values = lab_test.objects.get(id=id)
        values.send_doctor_lab_report = True
        values.save()
        messages.info(request, "successfully sent ")
        return redirect('/view_lab_test/')


def lab_logout(request):
    if 'lab' in request.session:
        request.session.pop('lab',None)
        messages.success(request,'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/lab_logout/')
