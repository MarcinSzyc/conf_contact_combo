from django.forms import ModelForm, DateInput, Textarea, TextInput, Select, MultiWidget
from contact_box.models import Person, Address, Email, PhoneNumber, Group
from django import forms


class PersonForm(ModelForm):
    class Meta:
        model = Person
        widgets = {
            'name': TextInput(attrs={'class': 'form-control mb-2 mr-sm-2'}),
            'last_name': TextInput(attrs={'class': 'form-control mb-2 mr-sm-2'}),
            'description': Textarea(attrs={'rows': 5, 'cols': 20, 'class': 'form-control mb-2 mr-sm-2'}),
            'address': Select(attrs={'class': 'form-control mb-2 mr-sm-2'})
        }
        exclude = []


class AddressForm(ModelForm):
    class Meta:
        model = Address
        widgets = {
            'city': TextInput(attrs={'class': 'form-control mb-2 mr-sm-2'}),
            'street': TextInput(attrs={'class': 'form-control mb-2 mr-sm-2'}),
            'home_number': TextInput(attrs={'class': 'form-control mb-2 mr-sm-2'}),
            'flat_number': TextInput(attrs={'class': 'form-control mb-2 mr-sm-2'})
        }
        exclude = []


class EmailForm(ModelForm):
    class Meta:
        model = Email
        widgets = {
            'email_address': TextInput(attrs={'class': 'form-control mb-2 mr-sm-2'}),
            'type': Select(attrs={'class': 'form-control mb-2 mr-sm-2'}),
            'person': Select(attrs={'class': 'form-control mb-2 mr-sm-2'})
        }
        exclude = []


class PhoneNumberForm(ModelForm):
    class Meta:
        model = PhoneNumber
        widgets = {
            'phone_number': TextInput(attrs={'class': 'form-control mb-2 mr-sm-2'}),
            'type': Select(attrs={'class': 'form-control mb-2 mr-sm-2'}),
            'person': Select(attrs={'class': 'form-control mb-2 mr-sm-2'})
        }
        exclude = []


class GroupForm(ModelForm):
    class Meta:
        model = Group
        widgets = {
            'name': TextInput(attrs={'class': 'form-control mb-2 mr-sm-2'}),
            'person': Select(attrs={'class': 'form-control mb-2 mr-sm-2'})
        }
        exclude = []



