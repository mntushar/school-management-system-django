from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import*
from .models import*


# Create sub-super admin
@login_required
def employeecreate(request):
    create_employee_form = CreateEmployeeForm()
    if request.method == 'POST':
        create_employee_form = CreateEmployeeForm(request.POST)
        if create_employee_form.is_valid():
            username = create_employee_form.cleaned_data['username']
            password = create_employee_form.cleaned_data['password']
            email = create_employee_form.cleaned_data['email']
            frist_name = create_employee_form.cleaned_data['frist_name']
            last_name = create_employee_form.cleaned_data['last_name']
            repert_password = create_employee_form.cleaned_data['repert_passeord']
            if password == repert_password:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.first_name = frist_name
                user.last_name = last_name
                user.save()
                return redirect('employeelist-site')
    context = {
        'create_employee_form':create_employee_form,
    }
    return render(request, 'create_employee.html', context)


#sub-super admin employee list
@login_required
def employeelist(request):
    employeelist = User.objects.filter(is_superuser=False)
    context = {
        'employeelist':employeelist,
    }
    return render(request, 'employee_list.html', context)


#delete employee
@login_required
def deleteemployee(request, pk):
    emp_obj = User.objects.get(id=pk)
    emp_obj.delete()
    return redirect('employeelist-site')





