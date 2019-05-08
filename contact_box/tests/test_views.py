from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from contact_box.models import Person, Address, PhoneNumber, Email, Group, MOBILE_TYPES, EMAIL_TYPE
from faker import Faker


class URLExistsTests(TestCase):
    def test_person_all_url_exists_at_desired_location(self):
        response = self.client.get('/contact_box/')
        self.assertEqual(response.status_code, 200)


class NotLoggedInTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        fake = Faker()
        cls.test_user = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        cls.test_user.save()
        cls.address = Address.objects.create(city=fake.city(),
                                             street=fake.street_name(),
                                             home_number=fake.random_number(),
                                             flat_number=fake.random_number()
                                             )
        cls.person = Person.objects.create(name=fake.first_name(),
                                           last_name=fake.last_name(),
                                           description=fake.text(),
                                           address=cls.address)

        cls.phone = PhoneNumber.objects.create(person=cls.person,
                                               phone_number=fake.isbn10(''),
                                               type=MOBILE_TYPES[0][0]
                                               )
        cls.email = Email.objects.create(person=cls.person,
                                         email_address=fake.email(),
                                         type=EMAIL_TYPE[0][0]
                                         )
        cls.group = Group.objects.create(name=fake.color_name())

    def test_new_person_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('contact_box:new_person'))
        self.assertRedirects(response, '/contact_box/?next=/contact_box/new/')

    def test_modify_person_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('contact_box:modify_person_view', kwargs={'id': self.person.pk}))
        self.assertRedirects(response, f'/contact_box/?next=/contact_box/modify/{self.person.pk}')

    def test_delete_person_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('contact_box:delete_person', kwargs={'id': self.person.pk}))
        self.assertRedirects(response, f'/contact_box/?next=/contact_box/delete/{self.person.pk}')

    def test_new_address_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('contact_box:new_address'))
        self.assertRedirects(response, '/contact_box/?next=/contact_box/new_address/')

    def test_new_phone_number_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('contact_box:new_phone_number'))
        self.assertRedirects(response, '/contact_box/?next=/contact_box/new_phone_number/')

    def test_new_email_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('contact_box:new_email'))
        self.assertRedirects(response, '/contact_box/?next=/contact_box/new_email/')

    def test_new_group_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('contact_box:new_group'))
        self.assertRedirects(response, '/contact_box/?next=/contact_box/new_group/')

    def test_delete_address_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('contact_box:delete_address', kwargs={'id': self.address.pk}))
        self.assertRedirects(response, f'/contact_box/?next=/contact_box/delete_address/{self.address.pk}')

    def test_delete_phone_number_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('contact_box:delete_phone', kwargs={'id': self.phone.pk}))
        self.assertRedirects(response, f'/contact_box/?next=/contact_box/delete_phone/{self.phone.pk}')

    def test_delete_email_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('contact_box:delete_email', kwargs={'id': self.email.pk}))
        self.assertRedirects(response, f'/contact_box/?next=/contact_box/delete_email/{self.email.pk}')

    def test_delete_group_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('contact_box:delete_group', kwargs={'id': self.group.pk}))
        self.assertRedirects(response, f'/contact_box/?next=/contact_box/delete_group/{self.group.pk}')
