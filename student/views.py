from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import*
from .models import*


#student list
@login_required
def studentlist(request):
    studentl = StudentDetailInfo.objects.all()
    forms = StudentSearchForm()
    if request.method == 'POST':
        forms = StudentSearchForm(request.POST)
        if forms.is_valid():
            sclass = forms.cleaned_data['sclass']
            sroll = forms.cleaned_data['sroll']
            if sroll is None:
                sstudentl = StudentDetailInfo.objects.filter(class_id__classname__icontains=sclass)
            else:
                sstudentl = StudentDetailInfo.objects.filter(roll=sroll, class_id__classname__icontains=sclass)
            context = {
                'studentlist' : sstudentl,
                'forms' : forms
            }
            return render(request, 'student_search.html', context)
    context = {
        'studentlist' : studentl,
        'forms' : forms

    }
    return render(request, 'student.html', context)
    

#add student
@login_required
def addstudent(request):
    forms1 = StudentInfoForm()
    forms2 = StudentDetailInfoForm()
    if request.method == 'POST':
        forms1 = StudentInfoForm(request.POST)
        forms2 = StudentDetailInfoForm(request.POST)
        if  forms1.is_valid() and forms2.is_valid():
            forms1_obj = forms1.save()
            forms2_obj = forms2.save(commit=False)
            forms2_obj.student = forms1_obj
            forms2.save()
            return redirect('studentlist-site')


    context = {
        'forms1' : forms1,
        'forms2' : forms2,
    }
    return render(request, 'add_student.html', context)


#edit student profile
@login_required
def studentedit(request, pk):
    std_det = StudentDetailInfo.objects.get(id=pk)
    std_info = std_det.student
    forms1 = StudentInfoForm(instance=std_info)
    forms2 = StudentDetailInfoForm(instance=std_det)
    if request.method == 'POST':
        forms1 = StudentInfoForm(request.POST, instance=std_info)
        forms2 = StudentDetailInfoForm(request.POST, instance=std_det)
        if  forms1.is_valid() and forms2.is_valid():
            forms1_obj = forms1.save()
            forms2_obj = forms2.save(commit=False)
            forms2_obj.student = forms1_obj
            forms2.save()
            return redirect('studentlist-site')


    context ={
        'forms1' : forms1,
        'forms2' : forms2,

    }
    
    return render(request,'edit_student.html', context)


#delete student profile
@login_required
def studentdelete(request, pk):
    studentinfo_obj = StudentInfo.objects.get(id=pk)
    studentinfo_obj.delete()
    return redirect('studentlist-site')


# student attendance view
@login_required
def std_att_view(request):
    std_search_forms = StudentsAttendanceForm()
    if request.method == 'POST':
        std_search_forms = StudentsAttendanceForm(request.POST)
        if  std_search_forms.is_valid():
            std_class = std_search_forms.cleaned_data['std_class']
            studentl = StudentDetailInfo.objects.filter(class_id__classshortname=std_class)
            contex = {
                'studentl':studentl,
                'std_search_forms':std_search_forms,
            }
            return render(request, 'student/attendance_view.html', contex)
            
    contex = {
        'std_search_forms':std_search_forms,
    }
    return render(request, 'student/attendance_view.html', contex)
    

