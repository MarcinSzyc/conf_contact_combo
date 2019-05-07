from django.test import TestCase


class ContactBoxEndpointsTests(TestCase):

    # Person views
    def test_all_person_view(self):
        response = self.client.get('/contact_box/', format='json')
        self.assertEqual(response.status_code, 200)

    def test_new_person_view(self):
        response = self.client
        response.login(username='admin', password='Django.11')
        response2 = self.client.get('/contact_box/new/', format='json')
        self.assertEqual(response2.status_code, 200)

    def test_modify_person_view(self):
        response = self.client.get('/contact_box/modify/1', format='json')
        self.assertEqual(response.status_code, 200)

    def test_delete_person_view(self):
        response = self.client.get('/contact_box/delete/1', format='json')
        self.assertEqual(response.status_code, 200)

    # Email views
    def test_new_email_address_view(self):
        response = self.client.get('/contact_box/new_email/', format='json')
        self.assertEqual(response.status_code, 200)
