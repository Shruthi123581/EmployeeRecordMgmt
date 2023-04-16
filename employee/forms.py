from .models import Employees,Project,Profile, Task
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class EmployeeRegistration(forms.ModelForm):
    
    class Meta:
        model = Employees
        fields = ["empid","name","job","email","phone","role"]
        widgets = {
            'empid' : forms.TextInput(attrs={'class':'form-control'}),
            'name'  : forms.TextInput(attrs={'class':'form-control'}),
            'job'   : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
        }


class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        
        fields = ['name', 'email', 'address', 'role']
        
#The labels attribute is optional. It is used to define the labels of the form fields created   
      #  labels = {
      #          "name":("Name     "),
       #         "email":("Email Address"),
       #         "address":("Street Address"),
       #         }
        
        widgets = {
            
            'name'  : forms.TextInput(attrs={'class':'form-control'}),  
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
        }


class CreteUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            
            'username'  : forms.TextInput(attrs={'class':'form-control'}),  
             'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'password1' : forms.PasswordInput(attrs={'class':'form-control'}),
            'password2' : forms.PasswordInput(attrs={'class':'form-control'}),
            
            
        }
        
class ProjectCrete(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['ptitle','pdesc', 'name']
        widgets = {
            'ptitle' : forms.TextInput(attrs={'class':'form-control'}),
            'pdesc'  : forms.TextInput(attrs={'class':'form-control'}),
            
        }
        

class TaskCreate(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['ptitle', 'name', 'status']
        widgets = {
            'ptitle' : forms.TextInput(attrs={'class':'form-control'}),
            'name'  : forms.TextInput(attrs={'class':'form-control'}),
        
        }