from django.urls import path
from . import views

urlpatterns = [
    path('studentlist/', views.studentlist, name='studentlist-site'), #student list url
    path('addstudent/', views.addstudent, name='addstudent-site'), #student register url
    path('studentlist/editstudent/<int:pk>/', views.studentedit, name='editstudent-site'), #student profile edit url
    path('deletestudent/<int:pk>/', views.studentdelete, name='deletehstudent-site'), #student delete url
    path('attendance/', views.std_att_view, name='attendance-site'), #student attendance url
    
]