from django.urls import include, path
from .import views

urlpatterns = [
    path('profile', views.adminprofile, name='adminprofile-site'), #admin profile url
    path('editadmin', views.adminedit, name='editadmin-site'), #admin profile edit url
    path('changepass', views.changepassword, name='changepass-site'), #admin password change url
    
]