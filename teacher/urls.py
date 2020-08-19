from django.urls import path
from .import views

urlpatterns = [
    path('teacherlist/', views.teacherlist, name='teacherlist-site'), #teacher list url
    path('addteacher/', views.teacherformsview, name='addteacher-site'), #teacher registration url
    path('teacheredit/<int:teacher_id>/', views.teacher_edit, name='teacheredit-site'), #teacher profile edit url
    path('teacheredelete/<int:teacher_id>/', views.teacher_delete, name='teacheredelete-site'), #teacher delete url
    
]