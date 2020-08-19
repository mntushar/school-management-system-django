from django.urls import path
from . import views

urlpatterns = [
    path('attendance/<std_class>/<std_roll>', views.std_attendance, name='studentattendance-site'), #api attendance url
    path('attendancecl/<std_class>/<std_roll>', views.std_att_class.as_view(), name='studentattendance-site'), #class base view api attendance url
    path('result/', views.result_student.as_view(), name='studentresult-site'), #student result api url
    path('student/create/', views.CreateStudentDetail.as_view(), name='studentcreate-site'), #student create api url
    path('student/view/', views.StudentView.as_view(), name='studentview-site'), #all student view api url
    path('student/create/mul', views.MulStudentDetail.as_view(), name='mulstudentcreate-site'), #multiple student create api url
    path('student/view/<int:pk>', views.ViewStudent.as_view(), name='single_student_view-site'), #single student view api url
    
]