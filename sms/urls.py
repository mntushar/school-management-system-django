"""sms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views as Token
from .import views
from admins.views import user_loging, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loginuser/', user_loging, name='userlogin-site'), #user loging url
    path('logoutuser/', user_logout, name='userlogout-site'), #user logout url
    path('', views.home, name='home'), #user dashboard url
    path('teacher/', include('teacher.urls'), name='teacher-site'), #teacher section url
    path('student/', include('student.urls'), name='student-site'), #student section url
    path('employee/', include('employee.urls'), name='employee-site'), #employee section url
    path('admins/', include('admins.urls'), name='admins-site'), #user admin section url
    path('api/', include('API.urls'), name='api-site'), #api section url
    
]


#api authentication token create 
urlpatterns += [
    path('api-token-auth/', Token.obtain_auth_token)
]
