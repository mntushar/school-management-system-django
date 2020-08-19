from django.urls import include, path
from .import views

urlpatterns = [
    path('createemployee/', views.employeecreate, name='create-employee-site'), #create employee url
    path('employeelist/', views.employeelist, name='employeelist-site'), #employee list url
    path('employeeedelete/<int:pk>/', views.deleteemployee, name='deleteemployee-site'), #delete employee url
]