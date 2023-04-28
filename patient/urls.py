from django.urls import path
from. import views

urlpatterns = [

    path('patient_login/',views.patient_login, name="patient_login"),
    path('patient_register/', views.patient_register, name='patient_register'),
    path('patient_home/', views.patient_home, name='patient_home'),
    path('basic_patient_details/', views.basic_patient_details, name='basic_patient_details'),
    path('view_patient_details/', views.view_patient_details, name='view_patient_details'),
    path('apply_medical_details/', views.apply_medical_details, name='apply_medical_details'),
    path('patient_logout/', views.patient_logout, name='patient_logout'),
    path('send_basic_details/<int:id>/', views.send_basic_details, name='send_basic_details'),
    path('send_medical_details/<int:id>/', views.send_medical_details, name='send_medical_details'),
    path('final/',views.final),
    path('mail/', views.mail),
    path('sendmail/<int:id>/',views.sendmail)



    ]