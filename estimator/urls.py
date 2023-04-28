from django.urls import path,include
from. import views

urlpatterns = [
    path('estimator_home/', views.estimator_home, name='estimator_home'),
    path('estimator_register/', views.estimator_register, name='estimator_register'),
    path('estimator_login/', views.estimator_login, name='estimator_login'),
    path('view_pat_labtest_medical_details/',views.view_pat_labtest_medical_details, name='view_pat_labtest_medical_details'),
    path('estimator_logout/', views.estimator_logout, name='estimator_logout'),
    path('get_report/<int:id>/', views.get_report, name='get_report'),
    path('viewfinal/',views.viewfinal),
    path('send/<int:id>/',views.send)
]