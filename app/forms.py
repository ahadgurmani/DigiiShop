from django import forms
from django.contrib.auth.models import User
from .models import Costumer
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm,SetPasswordForm


########sign up form########

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget= forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget= forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField( required= True, label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}

## Costumer Form ###
class CostumerForm(forms.ModelForm):
    class Meta:
        model = Costumer
        fields = ['id','name', 'father_name','city', 'locality']


########## Password change ###########

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs= {'class': 'form-control'}))
    new_password2 = forms.CharField(label='Confirm(New Password)', widget=forms.PasswordInput(attrs= {'class': 'form-control'}))


######## Password Reset ################

class Password_ResetForm(PasswordResetForm):
    email =  forms.CharField( required= True, label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))


######### Reset PassWord confirm New ######

class ResetConfirm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label= 'New Password(Confirm)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
