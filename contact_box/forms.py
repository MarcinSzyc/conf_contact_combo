from django.forms import ModelForm, DateInput, Textarea
from contact_box.models import Person, Address, Email, PhoneNumber, Group
from django import forms


class PersonForm(ModelForm):
    class Meta:
        model = Person
        widgets = {
            'description': Textarea(attrs={'rows': 5, 'cols': 20}),
        }
        exclude = []


class AddressForm(ModelForm):
    class Meta:
        model = Address
        exclude = []


class EmailForm(ModelForm):
    class Meta:
        model = Email
        exclude = []


class PhoneNumberForm(ModelForm):
    class Meta:
        model = PhoneNumber
        exclude = []


class GroupForm(ModelForm):
    class Meta:
        model = Group
        exclude = []


class UserLogin(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)
