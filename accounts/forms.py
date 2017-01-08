from django import forms
from django.contrib.auth.models import User

#Create your forms here
class RegistrationUserForm(forms.Form):
    firstname = forms.CharField(label='Firstname', max_length=50)
    lastname = forms.CharField(label='Lastname', max_length=50)
    username = forms.CharField(label='Username', min_length=2)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', min_length=4, widget=forms.PasswordInput())
    password_confirm = forms.CharField(label='Confirm password', widget=forms.PasswordInput)


    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nombre de usuario ya registrado.')
        return username


    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Ya existe un email igual en la db.')
        return email


    def clean_password_confirm(self):
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']
        if password != password_confirm:
            raise forms.ValidationError('Las contrasenas no coinciden.')
        return password_confirm

