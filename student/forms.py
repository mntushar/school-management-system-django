from django import forms
from django.forms import ModelForm
from .models import StudentInfo,StudentDetailInfo

#student information form
class StudentInfoForm(ModelForm):
     class Meta:
         model = StudentInfo
         fields = '__all__'
         widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'father': forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'address': forms.Textarea(attrs={'class':'form-control', 'required':'True'}),
        }


#student detail information form
class StudentDetailInfoForm(ModelForm):
     class Meta:
         model = StudentDetailInfo
         fields = ['roll', 'shiftid', 'class_id', 'section'] 
         labels = {
             'class_id' : 'class name',
             'shiftid': 'Shift name'

         }
         widgets = {
            'roll': forms.NumberInput(attrs={'class':'form-control', 'required':'True'}), 
            'shiftid': forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'class_id': forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'section': forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            
        }


#student search form
class StudentSearchForm(forms.Form):
    sroll = forms.IntegerField(
        label = 'Designation',
        required=False,
        widget=forms.NumberInput(attrs={'class':"form-control", 'placeholder':"Enter roll"})
        )
    sclass = forms.CharField(
        max_length=50,
        label = 'Name',
        required=False,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Class'})
        )


#student attendance form
class StudentsAttendanceForm(forms.Form):
    std_class = forms.CharField(
        max_length=10,
        label = 'Class name(Number value)',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Class', 'required':'True'})
        )
    