from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from faker import Faker


class TestLogin(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('general/chromedriver')
        self.fake = Faker()

    def tearDown(self):
        self.browser.close()

    def test_login(self):
        self.browser.get("http://localhost:8000/conf_rooms_reservations/address/")

        self.browser.find_element_by_css_selector('a:link#login').click()
        self.browser.implicitly_wait(1)
        self.browser.find_element_by_id('id_username_field').send_keys('admin')
        self.browser.find_element_by_id('id_password').send_keys('Django.11')
        self.browser.find_element_by_css_selector('#div_id_password  + button').click()
        self.browser.implicitly_wait(1)
        self.assertEquals(
            self.browser.find_element_by_css_selector('.alert').text,
            'Hello admin !!'
        )

    def test_registration(self):
        self.browser.get("http://localhost:8000/conf_rooms_reservations/address/")

        self.browser.find_element_by_link_text('Register').click()
        self.browser.implicitly_wait(1)
        self.browser.find_element_by_css_selector('input[name=username]').send_keys(self.fake.user_name())
        self.browser.find_element_by_id('id_email').click()
        self.browser.find_element_by_id('id_email').clear()
        self.browser.find_element_by_id('id_email').send_keys('mailik@host.pl')
        password = self.fake.password()
        self.browser.find_element_by_id('id_password1').send_keys(password)
        self.browser.find_element_by_id('id_password2').send_keys(password)
        self.browser.find_element_by_css_selector('#div_id_password2  + button').click()
        self.assertEquals(
            self.browser.find_element_by_css_selector('.alert').text,
            'User created!'
        )

    def test_room_search_link_directs_correctly(self):
        self.browser.get("http://localhost:8000/conf_rooms_reservations")

        self.browser.find_element_by_link_text('Room Search').click()
        self.assertEquals(
            self.browser.current_url,
            'http://localhost:8000/conf_rooms_reservations/search/')
