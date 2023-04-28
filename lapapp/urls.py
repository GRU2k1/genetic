from django.urls import path
from. import views

urlpatterns = [
    path('lab_register/', views.lab_register, name='lab_register'),
    path('lab_login/', views.lab_login, name='lab_login'),
    path('lab_home/', views.lab_home, name='lab_home'),
    path('lab_patient_basic_medical_details/', views.lab_patient_basic_medical_details, name='lab_patient_basic_medical_details'),
    path('lab_test_patient/', views.lab_test_patient, name='lab_test_patient'),
    path('view_lab_test/', views.view_lab_test, name='view_lab_test'),
    path('lab_details/', views.lab_details, name='lab_details'),
    path('lab_logout/', views.lab_logout, name='lab_logout'),
    path('send_to_doctor_labtest/<int:id>/', views.send_to_doctor_labtest, name='send_to_doctor_labtest')
    # path('patient_login/',views.patient_login, name="patient_login")
    ]