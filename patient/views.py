from django.shortcuts import render, redirect
from . models import *
from doctor.models import *
from django.db import IntegrityError
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def patient_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            r = patientRegister.objects.get(email=email, password=password,admin_approve=True)
            request.session['patient'] = r.email
            print(request.session['patient'])
            if r.admin_approve==1:
                messages.info(request, 'login successfuly')
                return redirect('/patient_home/')

            else:
                messages.info(request, 'Login access after admin approves')
                return redirect('/patient_login/')
        except patientRegister.DoesNotExist as e:
            messages.info(request, 'name does not exists')
            return redirect('/patient_login/')

    else:
        return render(request, 'patient/login.html')


def patient_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        Address = request.POST['Address']
        Dateofbirth = request.POST['Dateofbirth']
        phoneno = request.POST['phoneno']
        password = request.POST['password']
        try:
            patientRegister(username=username, email=email, Address=Address, Dateofbirth=Dateofbirth, phoneno=phoneno,
                   password=password).save()
            messages.info(request, "successfully created")
            return redirect('/patient_login/')
        except IntegrityError as e:
            messages.info(request, "name already exists")
            return redirect('/patient_register/')
    return render(request, 'patient/register.html')


def patient_home(request):
    return render(request,'patient/home_patent.html')


def basic_patient_details(request):
    if request.method == 'POST':
        basic = patientRegister.objects.get(email=request.session['patient'])
        patient_de = patient_detail()
        patient_de.firstname = basic.username
        patient_de.email = basic.email
        patient_de.phone_no = basic.phoneno
        patient_de.Date_of_birth = basic.Dateofbirth
        patient_de.Address = basic.Address
        patient_de.lastname = request.POST.get('lastname')
        patient_de.Gender = request.POST.get('Gender')
        patient_de.Age = request.POST.get('Age')
        patient_de.Marital_status = request.POST.get('Marital_status')
        patient_de.subject = request.POST.get('subject')
        patient_de.save()
        messages.info(request, "Your appointment registered")
        return redirect('/patient_home/')
    return render(request, 'patient/detail.html')


def view_patient_details(request):
    basic_data = patient_detail.objects.filter(send_basic_doctor=False)
    medical_data = patient_medical_details.objects.filter(send_medi_doctor=False)
    return render (request, 'patient/patient_basic_details.html',{'basic_data':basic_data,'medical_data':medical_data})


def apply_medical_details(request):
    if request.method == 'POST':
        basic = patient_detail.objects.get(email=request.session['patient'])
        medical = patient_medical_details()
        medical.name = basic.firstname
        medical.Gender = basic.Gender
        medical.age=basic.Age
        medical.Martial_status=basic.Marital_status
        medical.height=request.POST.get('height')
        medical.weight = request.POST.get('weight')
        medical.blood_type = request.POST.get('blood_type')
        medical.blood_count = request.POST.get('blood_count')
        medical.symptoms = request.POST.get('symptoms')
        medical.save()
        return redirect('/patient_home/')
    return render(request,'patient/medical_form.html')


def patient_logout(request):
    if 'patient' in request.session:
        request.session.pop('patient',None)
        messages.success(request,'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/patient_logout/')


def send_basic_details(request,id):
    if "patient" in request.session:
        basic_data = patient_detail.objects.get(id=id)
        basic_data.send_basic_doctor= True
        basic_data.save()
        print('hi')
        messages.info(request, "successfully sent to Doctor")
    return redirect('/view_patient_details/')


def send_medical_details(request,id):
    if "patient" in request.session:
        medical_data = patient_medical_details.objects.get(id=id)
        medical_data.send_medi_doctor = True
        medical_data.save()
        print('hi')
        messages.info(request, "successfully sent to Doctor")
    return redirect('/view_patient_details/')



def final(request):
    lab_data = lab_test.objects.filter(send2=True)
    return render(request, 'patient/estimator_patient.html', {'lab_data': lab_data})


def mail(request):
    basic = patientRegister.objects.filter(second_approve=False)
    return render(request,'patient/mail.html',{'basic':basic})


def sendmail(request, id):
    basic = patientRegister.objects.get(id=id)
    data = doctorRegister.objects.all()
    basic1 = lab_test.objects.get(email=request.session['patient'])
    datas=[]


    for i in data:
        datas.append(i.email)
        print('1',i.email)
    print('2',datas[-1])
    k = datas[-1]
    print('3',k)
    # print(datas.username)

    # print(datas.email)
    # print(datas.refer)
    var1=basic1.name
    subject="hi"+"_"+ var1+"!!!"
    send_mail(
        subject,
        basic1.output,
        basic1.email,
        [k],
        fail_silently=False,
    )
    print('hi4')

    basic.second_approve = True
    print('hi')
    basic.save()
    messages.info(request, "view report")
    return redirect('/mail/')

# def ok (request):
#     lab_data = patientRegister.objects.filter(second_approve=True)
#     return render(request, 'patient/estimator_patient.html', {'lab_data': lab_data})
#
#
# def view_ok(request,id):
#     if "patient" in request.session:
#         medical_data = patientRegister.objects.get(id=id)
#         medical_data.second_approve = True
#         medical_data.save()
#         print('hi')
#         messages.info(request, "view report")
#     return redirect('/final/')

# import imghdr
# message = EmailMessage()
# message['Subject'] = "email_subject"
# message['From'] = "demosample178@gmail.com"
# message['To'] = data.email
#
# with open(path, 'rb') as file:
#     image_data = file.read()
#
# message.set_content("Email from Python with image attachment")
#
# message.add_attachment(image_data, maintype='image', subtype=imghdr.what(None, image_data))
# server = smtplib.SMTP("smtp.gmail.com" ,587)
#
# server.ehlo()
#
# server.starttls()
#
#
# server.login("demosample178@gmail.com", "owiixglnlbxwogcs")
#
# server.send_message(message)
#
# server.quit()
