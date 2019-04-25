from contact_box.models import Person, PhoneNumber, MOBILE_TYPES, Address, Group, Email, EMAIL_TYPE
from faker import Faker
from random import choice, randint


def populate_initial_data():
    fake = Faker()
    person_instance = Person(name=fake.first_name(), last_name=fake.last_name(), description=fake.text())
    phone_instance = PhoneNumber(phone_number=fake.isbn10(''), type=choice(MOBILE_TYPES)[0])
    address_instance = Address(city=fake.city(), street=fake.street_name(), home_number=randint(0, 1000),
                               flat_number=randint(0, 100))
    email_instance = Email(email_address=fake.email(), type=choice(EMAIL_TYPE)[0])
    try:
        person_instance.save()
        phone_instance.save()
        address_instance.save()
        email_instance.save()
    except:
        pass


def create_groups():
    fake = Faker()
    group_instance = Group(name=fake.color_name())
    group_instance.save()


def add_address_to_person(person, address):
    person.address = address
    person.save()


def add_email_to_person(person, email):
    email.person = person
    email.save()


def add_phone_to_person(person, phone):
    phone.person = person
    phone.save()


def add_group_to_person(person, group):
    group.person.add(person)
