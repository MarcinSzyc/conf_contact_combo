from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from conference_rooms_reservations.models import Room, Reservation
from faker import Faker
from random import randint


class URLExistsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        fake = Faker()
        cls.room = Room.objects.create(name=fake.color_name(),
                                       capacity=randint(1, 100),
                                       projector=fake.boolean())

    def test_layout_url_exists_at_desired_location(self):
        response = self.client.get('/conf_rooms_reservations/')
        self.assertRedirects(response, '/conf_rooms_reservations/address/')

    def test_all_rooms_url_exists_at_desired_location(self):
        response = self.client.get('/conf_rooms_reservations/address/')
        self.assertEquals(response.status_code, 200)

    def test_info_view_url_exists_at_desired_location(self):
        response = self.client.get(f'/conf_rooms_reservations/room/info/{self.room.pk}')
        self.assertEquals(response.status_code, 200)

    def test_reservation_view_url_exists_at_desired_location(self):
        response = self.client.get(f'/conf_rooms_reservations/reservation/{self.room.pk}')
        self.assertEquals(response.status_code, 200)

    def test_room_search_view_url_exists_at_desired_location(self):
        response = self.client.get('/conf_rooms_reservations/search/')
        self.assertEquals(response.status_code, 200)


class NotLoggedInTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        fake = Faker()
        cls.room = Room.objects.create(name=fake.color_name(),
                                       capacity=randint(1, 100),
                                       projector=fake.boolean())
        cls.reservation = Reservation(date=fake.date_between(start_date='today', end_date='+30d'),
                                      comment=fake.text(),
                                      room=cls.room)

    def test_room_add_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('conference_rooms_reservations:add_room'))
        self.assertRedirects(response, '/conf_rooms_reservations/address/?next=/conf_rooms_reservations/room/add')

    def test_room_modify_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('conference_rooms_reservations:modify_room', kwargs={'id': self.room.pk}))
        self.assertRedirects(response,
                             f'/conf_rooms_reservations/address/?next=/conf_rooms_reservations/room/modify/{self.room.pk}')

    def test_room_delete_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('conference_rooms_reservations:delete_room', kwargs={'id': self.room.pk}))
        self.assertRedirects(response,
                             f'/conf_rooms_reservations/address/?next=/conf_rooms_reservations/room/delete/{self.room.pk}')
