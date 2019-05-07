from django.test import TestCase
from conference_rooms_reservations.models import Reservation, Room
from faker import Faker
from random import randint


class RoomTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        fake = Faker()
        cls.room = Room.objects.create(name=fake.color_name(),
                                       capacity=randint(1, 100),
                                       projector=fake.boolean()
                                       )

    def test_room_name_label(self):
        field_label = self.room._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'room name')

    def test_capacity_label(self):
        field_label = self.room._meta.get_field('capacity').verbose_name
        self.assertEquals(field_label, 'room capacity')

    def test_projector_label(self):
        field_label = self.room._meta.get_field('projector').verbose_name
        self.assertEquals(field_label, 'projector')

    def test_room_name_max_length(self):
        max_length = self.room._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_capacity_default_value(self):
        default_value = self.room._meta.get_field('capacity').default
        self.assertEquals(default_value, 0)

    def test_capacity_blank_false(self):
        blank_value = self.room._meta.get_field('capacity').blank
        self.assertFalse(blank_value)

    def test_projector_field_blank_true(self):
        blank_value = self.room._meta.get_field('projector').blank
        self.assertTrue(blank_value)

    def test_room_name_return_room_name(self):
        expected_object_name = f'{self.room.name}'
        self.assertEquals(expected_object_name, str(self.room))


class ReservationTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        fake = Faker()
        cls.room = Room.objects.create(name=fake.color_name(),
                                       capacity=randint(1, 100),
                                       projector=fake.boolean()
                                       )
        cls.reservation = Reservation.objects.create(
            date=fake.date_between(start_date='today', end_date='+30d'),
            comment=fake.text(),
            room=cls.room
        )

    def test_reservation_date_label(self):
        field_label = self.reservation._meta.get_field('date').verbose_name
        self.assertEquals(field_label, 'reservation date')

    def test_reservation_comment_label(self):
        field_label = self.reservation._meta.get_field('comment').verbose_name
        self.assertEquals(field_label, 'comment')

    def test_reservation_room_label(self):
        field_label = self.reservation._meta.get_field('room').verbose_name
        self.assertEquals(field_label, 'room')

    def test_date_blank_false(self):
        blank_value = self.reservation._meta.get_field('date').blank
        self.assertFalse(blank_value)

    def test_comment_field_blank_true(self):
        blank_value = self.reservation._meta.get_field('comment').blank
        self.assertTrue(blank_value)

    def test_room_field_blank_false(self):
        blank_value = self.reservation._meta.get_field('room').blank
        self.assertFalse(blank_value)

    def test_date_validators(self):
        validator_name = self.reservation._meta.get_field('date').validators
        self.assertEquals(validator_name[0].__name__, 'validate_date')

    def test_reservation_name_returns_room_space_date(self):
        expected_object_name = f'{self.reservation.room} {self.reservation.date}'
        self.assertEquals(expected_object_name, str(self.reservation))
