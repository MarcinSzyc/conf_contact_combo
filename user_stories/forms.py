from django.forms import ModelForm, DateInput
from user_stories.models import Person, Address, Email, PhoneNumber


class PersonForm(ModelForm):
    class Meta:
        model = Person
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
