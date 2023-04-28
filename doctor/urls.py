from django.urls import path,include
from. import views

urlpatterns = [
    path('doctor_login/', views.doctor_login, name='doctor_login'),
    path('doctor_home/', views.doctor_home, name='doctor_home'),
    path('doctor_register/', views.doctor_register, name='doctor_register'),
    path('doctor_logout/', views.doctor_logout, name='doctor_logout'),
    path('send_lab_medical_details/<int:id>/', views.send_lab_medical_details),
    path('send_lab_basic_details/<int:id>/', views.send_lab_basic_details,name='send_lab_basic_details'),

    path('view_patient_basic_medical_details/', views.view_patient_basic_medical_details, name='view_patient_basic_medical_details'),
    path('view_patient_labtest_medical_details/', views.view_patient_labtest_medical_details),
    path('estimatorview/',views.estimatorview),
    path('sendp/<int:id>/',views.sendp)
    ]