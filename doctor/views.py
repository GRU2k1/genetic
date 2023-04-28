from django.shortcuts import render, redirect
from . models import *
from django.db import IntegrityError
from django.contrib import messages
from patient.models import *
from django.core.mail import send_mail
from django.conf import settings


def doctor_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            r = doctorRegister.objects.get(email=email, password=password,admin_approve=True)
            request.session['doctor'] = r.email
            print(request.session['doctor'])
            if r is not None:
                messages.info(request, 'welcome')
                return redirect('/doctor_home/')
        except doctorRegister.DoesNotExist as e:
            messages.info(request, 'name does not exists')
            return redirect('/doctor_login/')

    else:
        return render(request, 'doctor/login.html')


def doctor_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        Address = request.POST['Address']
        Dateofbirth = request.POST['Dateofbirth']
        phoneno = request.POST['phoneno']
        password = request.POST['password']
        try:
            doctorRegister(username=username, email=email, Address=Address, Dateofbirth=Dateofbirth, phoneno=phoneno,
                   password=password).save()
            messages.info(request, "successfully created")
            return redirect('/doctor_login/')
        except IntegrityError as e:
            messages.info(request, "name already exists")
            return redirect('/doctor_register/')
    return render(request, 'doctor/register.html')


def doctor_home(request):
    return render(request,'doctor/home_doctor.html')


def view_patient_basic_medical_details(request):
    basic_data = patient_detail.objects.filter(send_basic_doctor=True)
    medical_data = patient_medical_details.objects.filter(send_medi_doctor=True)
    return render (request, 'doctor/view.html',{'basic_data':basic_data,'medical_data':medical_data})


def doctor_logout(request):
    if 'doctor' in request.session:
        request.session.pop('doctor', None)
        messages.success(request, 'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/doctor_logout/')


def send_lab_basic_details(request,id):
    if "doctor" in request.session:
        print('hi')
        values = patient_detail.objects.get(id=id)
        values.send_basic_lab= True
        values.save()
        print('hi')
        messages.info(request, "successfully sent to lab")
        return redirect('/view_patient_basic_medical_details/')


def send_lab_medical_details(request,id):
    if "doctor" in request.session:
        print('hi')
        values = patient_medical_details.objects.get(id=id)
        values.send_medi_lab= True
        values.save()
        print('hi')
        messages.info(request, "successfully sent to lab")
        return redirect('/view_patient_basic_medical_details/')


def view_patient_labtest_medical_details(request):
    basic_data = patient_detail.objects.filter(send_basic_doctor=True)
    lab_data = lab_test.objects.filter(send_doctor_lab_report=True)
    return render (request, 'doctor/view_lab_test.html',{'basic_data':basic_data,'lab_data':lab_data})



def estimatorview(request):
    lab_data = lab_test.objects.filter(send=True)
    return render(request,'doctor/estimate_report.html',{'lab_data':lab_data})



def sendp(request,id):
    if "doctor" in request.session:
      lab_data = lab_test.objects.get(id=id)
      lab_data.send2=True
      lab_data.save()
      messages.info(request, "successfully sent to Patient")
      return redirect('/estimatorview/')