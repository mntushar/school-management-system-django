from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TeacherInfo
from .forms import TeacherForm, TeacherSearchForm


#teacher list
@login_required
def teacherlist(request):
    teacherl = TeacherInfo.objects.all()
    forms = TeacherSearchForm()
    if request.method == 'POST':
        forms = TeacherSearchForm(request.POST)
        if forms.is_valid():
            sname = forms.cleaned_data['sname']
            sdeg = forms.cleaned_data['sdeg']
            steacherl = TeacherInfo.objects.filter(name__iexact=sname, designation__iexact=sdeg)
            context = {
                'steacherl' : steacherl,
                'forms' : forms
            }
            return render(request, 'teacher_search.html', context)
    context = {
        'teacherlist' : teacherl,
        'forms' : forms

    }
    return render(request, 'teacher.html', context)

#teacher list
@login_required
def teacherformsview(request):
    forms = TeacherForm()
    if request.method == 'POST':
        forms = TeacherForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('teacherlist-site')
    context = {
        'forms' : forms
    }
    return render(request, 'add_teacher.html', context)


#teacher edit profile
@login_required
def teacher_edit(request, teacher_id):
    teacheredit = TeacherInfo.objects.get(id=teacher_id)
    forms = TeacherForm(instance=teacheredit)
    if request.method == 'POST':
        forms = TeacherForm(request.POST, instance=teacheredit)
        if forms.is_valid():
            forms.save()
            return redirect('teacherlist-site')
    context = {
        'forms' : forms
    }
    return render(request, 'rdit_teacher.html', context)


#delete teacher
@login_required
def teacher_delete(request, teacher_id):
    teacherdelete = TeacherInfo.objects.get(id=teacher_id)
    teacherdelete.delete()
    return redirect('teacherlist-site')


