from django.forms import ModelForm
from django import forms
from employee.models import*


#ereate employee form
class CreateEmployeeForm(forms.Form):
    username = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    password = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    repert_passeord = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    email = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    frist_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    
