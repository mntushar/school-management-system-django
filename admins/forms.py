from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


#admin password forms
class AdminPasswordForm(forms.Form):
    newpassword = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': True}))
    repertnewpassword = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': True}))


#admin profile edit forms
class AdminEditForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control', 'required':'True'}),
            'first_name': forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            
        }


#user loging forms
class UserLogingForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': True}))
    