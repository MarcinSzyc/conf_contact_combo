from django.core.management.base import BaseCommand
from contact_box.models import Person, PhoneNumber, Address, Group, Email
from general.contact_box_worker import populate_initial_data, create_groups, add_phone_to_person, add_group_to_person, \
    add_email_to_person, add_address_to_person
from random import choice


class Command(BaseCommand):
    help = 'Fill database with fake data'

    def handle(self, *args, **kwargs):
        for i in range(30):
            populate_initial_data()

        for i in range(10):
            for person in Person.objects.all():
                add_address_to_person(person, choice(Address.objects.all()))
                add_email_to_person(person, choice(Email.objects.all()))
                add_phone_to_person(person, choice(PhoneNumber.objects.all()))

        for i in range(10):
            create_groups()
            for person in Person.objects.all():
                add_group_to_person(person, choice(Group.objects.all()))
