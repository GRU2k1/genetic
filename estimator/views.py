from django.shortcuts import render, redirect
from . models import *
from doctor.models import *
from admins.models import *
from lapapp.models import *
from patient.models import *
from django.db import IntegrityError
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from estimator.models import *
import warnings
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier


from django.core.mail import send_mail
from django.contrib import messages
warnings.filterwarnings('ignore')
import random
from math import ceil
from decimal import Decimal
# from authority.models import *
# import services


def estimator_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            r = estimatorRegister.objects.get(email=email, password=password)
            request.session['estimator'] = r.email
            print(request.session['estimator'])
            if r is not None:
                messages.info(request, 'welcome')
                return redirect('/estimator_home/')
        except estimatorRegister.DoesNotExist as e:
            messages.info(request, 'name does not exists')
            return redirect('/estimator_login/')

    else:
        return render(request, 'estimator/login.html')


def estimator_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        Address = request.POST['Address']
        phoneno = request.POST['phoneno']
        Dateofbirth = request.POST['Dateofbirth']
        password = request.POST['password']
        try:
            estimatorRegister(username=username, email=email, Address=Address, phoneno=phoneno, Dateofbirth=Dateofbirth,
                   password=password).save()
            messages.info(request, "successfully created")
            return redirect('/estimator_login/')
        except IntegrityError as e:
            messages.info(request, "name already exists")
            return redirect('/estimator_register/')
    return render(request, 'estimator/register.html')


def estimator_home(request):
    return render(request,'estimator/home_estimator.html')


def view_pat_labtest_medical_details(request):
    lab_data = lab_test.objects.filter(send_doctor_lab_report=True)
    return render (request, 'estimator/pat_lab_test.html',{'lab_data':lab_data})


def algorithm(datas):
    data = pd.read_csv('new2.csv')
    data_x = data.iloc[:, :-1]
    data_y = data.iloc[:, -1]
    string_datas = [i for i in data_x.columns if data_x.dtypes[i] == np.object_]

    LabelEncoders = []
    for i in string_datas:
        newLabelEncoder = LabelEncoder()
        data_x[i] = newLabelEncoder.fit_transform(data_x[i])
        LabelEncoders.append(newLabelEncoder)
    ylabel_encoder = None
    if type(data_y.iloc[1]) == str:
        ylabel_encoder = LabelEncoder()
        data_y = ylabel_encoder.fit_transform(data_y)

    model = RandomForestClassifier()
    model.fit(data_x, data_y)
    value = {data_x.columns[i]: datas[i] for i in range(len(datas))}
    l = 0
    for i in string_datas:
        z = LabelEncoders[l]
        value[i] = z.transform([value[i]])[0]
        l += 1
    value = [i for i in value.values()]
    predicted = model.predict([value])
    if ylabel_encoder:
        predicted = ylabel_encoder.inverse_transform(predicted)
    return predicted[0]


def get_report (request,id):
    values = lab_test.objects.get(id=id)
    inputvar=[]
    r = values.id
    a = values.Genes_in_mothers_side
    b = values.Inherited_from_father
    c = values.Maternal_gene
    d = values.Paternal_gene
    e = values.Gender
    f = values.Birth_defects
    g = values.WhiteBlood_cell_count
    h = values.Blood_test_result

    inputvar.append(a)
    inputvar.append(b)
    inputvar.append(c)
    inputvar.append(d)
    inputvar.append(e)
    inputvar.append(f)
    inputvar.append(g)
    inputvar.append(h)
    print('input:',inputvar)
    a = algorithm(inputvar)
    print('OUTPUT:',a)
    st = lab_test.objects.filter(id=r).update(output=a)
    print(st)

    return redirect("/view_pat_labtest_medical_details/")


def estimator_logout(request):
    if 'estimator' in request.session:
        request.session.pop('estimator',None)
        messages.success(request,'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/estimator_logout/')


def viewfinal(request):
    lab_data = lab_test.objects.filter(send=False)
    return render(request,'estimator/viewfinal.html',{'lab_data':lab_data})

def send(request,id):
    if "estimator" in request.session:
     lab_data = lab_test.objects.get(id=id)
     lab_data.send=True
     lab_data.save()
     return redirect('/viewfinal/')

