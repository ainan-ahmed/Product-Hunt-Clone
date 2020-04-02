from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.core import validators
class UserCreateForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100','placeholder':'Password'})
                               ,validators=[validate_password])
    cpassword=forms.CharField(widget=forms.PasswordInput(),validators=[validate_password])
    class Meta:
        model = User
        fields = {'first_name','last_name','email','username','password'}
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'input100','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'input100','placeholder':'Last Name'}),
            'email':forms.EmailInput(attrs={'class':'input100','placeholder':'Email'}),
            'username':forms.TextInput(attrs={'class':'input100','placeholder':'Username'}),
        }
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).count() > 0:
            raise forms.ValidationError("We have a user with this user email-id")
        return data
    def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username=data).count() > 0:
            raise forms.ValidationError("We have a user with this username")
        return data
    
    