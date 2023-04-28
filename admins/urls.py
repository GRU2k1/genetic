from django.urls import path
from. import views

urlpatterns = [
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('approve_patient_details/', views.approve_patient_details, name='approve_patient_details'),
    path('approve_patient_true/<int:id>/', views.approve_patient_true, name='approve_patient_true'),
    path('approve_doctor_details/', views.approve_doctor_details, name='approve_doctor_details'),
    path('approve_doctor_true/<int:id>/',views.approve_doctor_true, name='approve_doctor_true'),
    path('approve_estimator_true/<int:id>/', views.approve_estimator_true, name='approve_estimator_true'),
    path('approve_estimator_details/', views.approve_estimator_details, name='approve_estimator_details'),
    path('approve_lab_test_details/', views.approve_lab_test_details,name='approve_lab_test_details'),
    path('approve_lab_test_true/<int:id>/', views.approve_lab_test_true, name='approve_lab_test_true')
    ]