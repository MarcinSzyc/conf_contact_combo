from django.forms import ModelForm, DateInput, Textarea, TextInput, Select, MultiWidget
from contact_box.models import Person, Address, Email, PhoneNumber, Group
from django import forms

class UserLogin(forms.Form):
    username = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control mb-2 mr-sm-2'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-2 mr-sm-2'}))