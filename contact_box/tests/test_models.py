from django.test import TestCase
from contact_box.models import Person, Address, Email, PhoneNumber, Group, EMAIL_TYPE, MOBILE_TYPES
from faker import Faker


class PersonTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        fake = Faker()
        cls.address = Address.objects.create(city=fake.city(),
                                             street=fake.street_name(),
                                             home_number=fake.random_number(),
                                             flat_number=fake.random_number()
                                             )
        cls.person = Person.objects.create(name=fake.first_name(),
                                           last_name=fake.last_name(),
                                           description=fake.text(),
                                           address=cls.address)

    def test_first_name_label(self):
        field_label = self.person._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_last_name_label(self):
        field_label = self.person._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_description_label(self):
        field_label = self.person._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_address_label(self):
        field_label = self.person._meta.get_field('address').verbose_name
        self.assertEquals(field_label, 'address')

    def test_first_name_max_length(self):
        max_length = self.person._meta.get_field('name').max_length
        self.assertEquals(max_length, 32)

    def test_last_name_max_length(self):
        max_length = self.person._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 32)

    def test_object_name_is_first_name_space_last_name(self):
        expected_object_name = f'{self.person.name} {self.person.last_name}'
        self.assertEquals(expected_object_name, str(self.person))


class AddressTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        fake = Faker()
        cls.address = Address.objects.create(city=fake.city(),
                                             street=fake.street_name(),
                                             home_number=fake.random_number(),
                                             flat_number=fake.random_number()
                                             )

    def test_city_label(self):
        field_label = self.address._meta.get_field('city').verbose_name
        self.assertEquals(field_label, 'city')

    def test_last_name_label(self):
        field_label = self.address._meta.get_field('street').verbose_name
        self.assertEquals(field_label, 'street name')

    def test_description_label(self):
        field_label = self.address._meta.get_field('home_number').verbose_name
        self.assertEquals(field_label, 'home number')

    def test_address_label(self):
        field_label = self.address._meta.get_field('flat_number').verbose_name
        self.assertEquals(field_label, 'flat number')

    def test_city_name_max_length(self):
        max_length = self.address._meta.get_field('city').max_length
        self.assertEquals(max_length, 32)

    def test_street_name_max_length(self):
        max_length = self.address._meta.get_field('street').max_length
        self.assertEquals(max_length, 64)


class PhoneNumberTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        fake = Faker()
        cls.person = Person.objects.create(name=fake.first_name(),
                                           last_name=fake.last_name(),
                                           description=fake.text(),
                                           address=None)
        cls.phone = PhoneNumber.objects.create(person=cls.person,
                                               phone_number=fake.isbn10(''),
                                               type=MOBILE_TYPES[0][0]
                                               )

    def test_phone_number_label(self):
        field_label = self.phone._meta.get_field('phone_number').verbose_name
        self.assertEquals(field_label, 'phone number')

    def test_phone_number_type_label(self):
        field_label = self.phone._meta.get_field('type').verbose_name
        self.assertEquals(field_label, 'phone type')


class EmailTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        fake = Faker()
        cls.person = Person.objects.create(name=fake.first_name(),
                                           last_name=fake.last_name(),
                                           description=fake.text(),
                                           address=None)
        cls.email = Email.objects.create(person=cls.person,
                                         email_address=fake.email(),
                                         type=EMAIL_TYPE[0][0]
                                         )

    def test_email_address_label(self):
        field_label = self.email._meta.get_field('email_address').verbose_name
        self.assertEquals(field_label, 'email address')

    def test_email_address_type_label(self):
        field_label = self.email._meta.get_field('type').verbose_name
        self.assertEquals(field_label, 'email type')


class GroupTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        fake = Faker()
        cls.group = Group.objects.create(name=fake.color_name())

    def test_group_label(self):
        field_label = self.group._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'group name')

    def test_group_name_max_length(self):
        max_length = self.group._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)
