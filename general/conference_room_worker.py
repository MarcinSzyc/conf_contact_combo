from conference_rooms_reservations.models import Reservation, Room
from faker import Faker
from random import choice, randint


def populate_room():
    fake = Faker()
    room_instance = Room(name=fake.color_name(), capacity=randint(1, 100), projector=fake.boolean())
    try:
        room_instance.save()
    except:
        pass


def populate_reservations():
    fake = Faker()
    reservation_instance = Reservation(date=fake.date_between(start_date='today', end_date='+30d'),
                                       comment=fake.text(), room=choice(Room.objects.all()))
    try:
        reservation_instance.save()
    except:
        pass
