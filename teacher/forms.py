from django import forms
from django.forms import ModelForm
from .models import TeacherInfo


#teacher registation form
class TeacherForm(ModelForm):
    class Meta:
        model = TeacherInfo
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'gender': forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'phonenumber': forms.NumberInput(attrs={'class':'form-control', 'required':'True'}),
            'designation': forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
        }


#teacher search form
class TeacherSearchForm(forms.Form):
    sname = forms.CharField(
        max_length=50,
        label = 'Name',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'})
        )
    sdeg = forms.CharField(
        max_length=20,
        label = 'Designation',
        widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"Depertment"})
        )
