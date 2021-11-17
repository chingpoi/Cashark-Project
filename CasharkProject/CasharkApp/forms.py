from django import forms
from .models import *

class RegisterForm(forms.Form):
    First_Name = models.CharField(max_length = 50)
    Last_Name = models.CharField(max_length = 50)
    Email = models.EmailField(max_length = 50, unique = True)
    Password = models.CharField(max_length = 50)
    Birthdate = models.CharField(max_length = 10)
    Mobile_Number = models.CharField(max_length = 50, unique = True)
    Address_Province = models.CharField(max_length = 50)
    Address_City = models.CharField(max_length = 50)
    Address_Street = models.CharField(max_length = 50)