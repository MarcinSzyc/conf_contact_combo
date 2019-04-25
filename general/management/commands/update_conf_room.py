from django.core.management.base import BaseCommand
from conference_rooms_reservations.models import Room, Reservation
from general.conference_room_worker import populate_reservations, populate_room


class Command(BaseCommand):
    help = 'Fill database with fake data'

    def handle(self, *args, **kwargs):
        for i in range(20):
            populate_room()

        for i in range(150):
            populate_reservations()
