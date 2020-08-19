from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .forms import*


#user loging
def user_loging(request):
    forms = UserLogingForm()
    if request.method == 'POST':
        forms = UserLogingForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            password = forms.cleaned_data['password']
            user = authenticate(username=name, password=password)
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    return redirect('home')
                else:
                    login(request, user)
                    return redirect('studentlist-site')
            else:
                error_loging = 'The email and password that you entered did not match our records. Please double-check and try again.'
                context = {
                    'error_loging':error_loging,
                    'forms':forms,
                }
                return render(request, 'admins/loging_user.html', context)
    context = {
        'forms': forms,
    }
    return render(request, 'admins/loging_user.html', context)
    


#user logout
def user_logout(request):
    logout(request)
    return redirect('userlogin-site')


#admin profile
@login_required
def adminprofile(request):
    user_a = User.objects.filter(is_superuser=True)
    user_a = user_a[0]
    contex = {
        'admin':user_a,
    }
    return render(request, 'admins/profile.html', contex)


#admin Edit profile
@login_required
def adminedit(request):
    user_a = User.objects.filter(is_superuser=True)
    user_a = user_a[0]
    print(user_a.first_name)
    forms = AdminEditForm(instance=user_a)
    if request.method == 'POST':
        forms = AdminEditForm(request.POST)
        if forms.is_valid():
            email = forms.cleaned_data['email']
            first_name = forms.cleaned_data['first_name']
            last_name = forms.cleaned_data['last_name']
            user_a.email = email
            user_a.first_name = first_name
            user_a.last_name = last_name
            user_a.save()
            return redirect('adminprofile-site')
    context = {
        'forms':forms,
    }
    return render(request, 'admins/edit_profile.html', context)


# change admin password
@login_required
def changepassword(request):
    user_a = User.objects.filter(is_superuser=True)
    user_a = user_a[0]
    form = AdminPasswordForm()
    if request.method == 'POST':
        forms = AdminPasswordForm(request.POST)
        if forms.is_valid():
            newp = forms.cleaned_data['newpassword']
            newrp = forms.cleaned_data['repertnewpassword']
            if newp == newrp:
                username = user_a.username
                user = User.objects.get(username=username)
                user.set_password(newp)
                user.save()
                return redirect('adminprofile-site')
    context = {
        'forms':form,
    }
    return render(request, 'admins/change_password.html', context)


