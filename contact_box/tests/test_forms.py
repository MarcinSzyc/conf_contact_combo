from django.test import TestCase
from contact_box.forms import PersonForm, AddressForm, EmailForm, PhoneNumberForm, GroupForm


class PersonFormTests(TestCase):

    def test_name_field_label(self):
        form = PersonForm()
        form_field = form.fields['name'].label
        self.assertEquals(form_field, 'First name')

    def test_last_name_field_label(self):
        form = PersonForm()
        form_field = form.fields['last_name'].label
        self.assertEquals(form_field, 'Last name')

    def test_description_field_label(self):
        form = PersonForm()
        form_field = form.fields['description'].label
        self.assertEquals(form_field, 'Description')

    def test_address_field_label(self):
        form = PersonForm()
        form_field = form.fields['address'].label
        self.assertEquals(form_field, 'Address')

    def test_for_name_field_widget(self):
        form = PersonForm()
        form_field = form.fields['name'].widget
        self.assertEquals(form_field.__class__.__name__, 'TextInput')

    def test_for_last_name_field_widget(self):
        form = PersonForm()
        form_field = form.fields['last_name'].widget
        self.assertEquals(form_field.__class__.__name__, 'TextInput')

    def test_for_description_field_widget(self):
        form = PersonForm()
        form_field = form.fields['description'].widget
        self.assertEquals(form_field.__class__.__name__, 'Textarea')

    def test_for_address_field_widget(self):
        form = PersonForm()
        form_field = form.fields['address'].widget
        self.assertEquals(form_field.__class__.__name__, 'Select')

    def test_for_correct_bootstrap_widget_attributes(self):
        form = PersonForm()
        name_field = form.fields['name'].widget
        capacity_field = form.fields['last_name'].widget
        projector_field = form.fields['description'].widget
        address_field = form.fields['address'].widget
        self.assertEquals(name_field.attrs['class'], 'form-control mb-2 mr-sm-2')
        self.assertEquals(capacity_field.attrs['class'], 'form-control mb-2 mr-sm-2')
        self.assertEquals(projector_field.attrs['class'], 'form-control mb-2 mr-sm-2')
        self.assertEquals(address_field.attrs['class'], 'form-control mb-2 mr-sm-2')

    def test_for_description_text_area_size(self):
        form = PersonForm()
        description_field = form.fields['description'].widget
        self.assertEquals(description_field.attrs['rows'], 5)
        self.assertEquals(description_field.attrs['cols'], 20)


class AddressFormTests(TestCase):

    def test_city_field_label(self):
        form = AddressForm()
        form_field = form.fields['city'].label
        self.assertEquals(form_field, 'City')

    def test_street_name_field_label(self):
        form = AddressForm()
        form_field = form.fields['street'].label
        self.assertEquals(form_field, 'Street name')

    def test_home_number_field_label(self):
        form = AddressForm()
        form_field = form.fields['home_number'].label
        self.assertEquals(form_field, 'Home number')

    def test_flat_number_field_label(self):
        form = AddressForm()
        form_field = form.fields['flat_number'].label
        self.assertEquals(form_field, 'Flat number')

    def test_for_city_field_widget(self):
        form = AddressForm()
        form_field = form.fields['city'].widget
        self.assertEquals(form_field.__class__.__name__, 'TextInput')

    def test_for_street_field_widget(self):
        form = AddressForm()
        form_field = form.fields['street'].widget
        self.assertEquals(form_field.__class__.__name__, 'TextInput')

    def test_for_home_number_field_widget(self):
        form = AddressForm()
        form_field = form.fields['home_number'].widget
        self.assertEquals(form_field.__class__.__name__, 'TextInput')

    def test_for_flat_number_field_widget(self):
        form = AddressForm()
        form_field = form.fields['flat_number'].widget
        self.assertEquals(form_field.__class__.__name__, 'TextInput')

    def test_for_correct_bootstrap_widget_attributes(self):
        form = AddressForm()
        city_field = form.fields['city'].widget
        street_field = form.fields['street'].widget
        home_number_field = form.fields['home_number'].widget
        flat_number_field = form.fields['flat_number'].widget
        self.assertEquals(city_field.attrs['class'], 'form-control mb-2 mr-sm-2')
        self.assertEquals(street_field.attrs['class'], 'form-control mb-2 mr-sm-2')
        self.assertEquals(home_number_field.attrs['class'], 'form-control mb-2 mr-sm-2')
        self.assertEquals(flat_number_field.attrs['class'], 'form-control mb-2 mr-sm-2')


class EmailFormTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.email_form = EmailForm()
        cls.email_address_field = cls.email_form.fields['email_address']
        cls.type_field = cls.email_form.fields['type']
        cls.person_field = cls.email_form.fields['person']
        cls.bootstrap_formatting = 'form-control mb-2 mr-sm-2'

    def test_email_field_label(self):
        form_field = self.email_address_field.label
        self.assertEquals(form_field, 'Email address')

    def test_type_field_label(self):
        form_field = self.type_field.label
        self.assertEquals(form_field, 'Email type')

    def test_person_label(self):
        form_field = self.person_field.label
        self.assertEquals(form_field, 'Person')

    def test_for_email_address_field_widget(self):
        form_field = self.email_address_field.widget
        self.assertEquals(form_field.__class__.__name__, 'TextInput')

    def test_for_type_field_widget(self):
        form_field = self.type_field.widget
        self.assertEquals(form_field.__class__.__name__, 'Select')

    def test_for_person_field_widget(self):
        form_field = self.person_field.widget
        self.assertEquals(form_field.__class__.__name__, 'Select')

    def test_for_correct_bootstrap_widget_attributes(self):
        self.assertEquals(self.email_address_field.widget.attrs['class'], self.bootstrap_formatting)
        self.assertEquals(self.type_field.widget.attrs['class'], self.bootstrap_formatting)
        self.assertEquals(self.person_field.widget.attrs['class'], self.bootstrap_formatting)


class PhoneNumberFormTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.phone_number_form = PhoneNumberForm()
        cls.phone_number_field = cls.phone_number_form.fields['phone_number']
        cls.type_field = cls.phone_number_form.fields['type']
        cls.person_field = cls.phone_number_form.fields['person']
        cls.bootstrap_formatting = 'form-control mb-2 mr-sm-2'

    def test_phone_number_field_label(self):
        form_field = self.phone_number_field.label
        self.assertEquals(form_field, 'Phone number')

    def test_type_field_label(self):
        form_field = self.type_field.label
        self.assertEquals(form_field, 'Phone type')

    def test_person_label(self):
        form_field = self.person_field.label
        self.assertEquals(form_field, 'Person')

    def test_for_phone_number_field_widget(self):
        form_field = self.phone_number_field.widget
        self.assertEquals(form_field.__class__.__name__, 'TextInput')

    def test_for_type_field_widget(self):
        form_field = self.type_field.widget
        self.assertEquals(form_field.__class__.__name__, 'Select')

    def test_for_person_field_widget(self):
        form_field = self.person_field.widget
        self.assertEquals(form_field.__class__.__name__, 'Select')

    def test_for_correct_bootstrap_widget_attributes(self):
        self.assertEquals(self.phone_number_field.widget.attrs['class'], self.bootstrap_formatting)
        self.assertEquals(self.type_field.widget.attrs['class'], self.bootstrap_formatting)
        self.assertEquals(self.person_field.widget.attrs['class'], self.bootstrap_formatting)


class GroupFormTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.group_form = GroupForm()
        cls.name_field = cls.group_form.fields['name']
        cls.person_field = cls.group_form.fields['person']
        cls.bootstrap_formatting = 'form-control mb-2 mr-sm-2'

    def test_name_field_label(self):
        form_field = self.name_field.label
        self.assertEquals(form_field, 'Group name')

    def test_person_label(self):
        form_field = self.person_field.label
        self.assertEquals(form_field, 'Person')

    def test_for_name_field_widget(self):
        form_field = self.name_field.widget
        self.assertEquals(form_field.__class__.__name__, 'TextInput')

    def test_for_person_field_widget(self):
        form_field = self.person_field.widget
        self.assertEquals(form_field.__class__.__name__, 'Select')

    def test_for_correct_bootstrap_widget_attributes(self):
        self.assertEquals(self.name_field.widget.attrs['class'], self.bootstrap_formatting)
        self.assertEquals(self.person_field.widget.attrs['class'], self.bootstrap_formatting)
