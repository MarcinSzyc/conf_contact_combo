from django.db import models

MOBILE_TYPES = (
    (0, "home"),
    (1, "mobile"),
    (2, "work"),
)

EMAIL_TYPE = (
    (0, "private"),
    (1, "work"),
)


class Person(models.Model):
    name = models.CharField('first name', max_length=32)
    last_name = models.CharField('last name', max_length=32)
    description = models.TextField('description', blank=True)
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, blank=False, null=True)

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Address(models.Model):
    city = models.CharField('city', max_length=32)
    street = models.CharField('street name', max_length=64)
    home_number = models.IntegerField('home number')
    flat_number = models.IntegerField('flat number', blank=True)

    def __str__(self):
        return f'{self.street} {self.home_number}; {self.city}'


class PhoneNumber(models.Model):
    person = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True)
    phone_number = models.IntegerField('phone number')
    type = models.IntegerField('phone type', choices=MOBILE_TYPES, default=1)

    def __str__(self):
        return f'{self.phone_number}'


class Email(models.Model):
    person = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True)
    email_address = models.EmailField('email address')
    type = models.IntegerField('email type', choices=EMAIL_TYPE, default=0)

    def __str__(self):
        return self.email_address


class Group(models.Model):
    name = models.CharField('group name', max_length=100, blank=False)
    person = models.ManyToManyField(Person)

    def __str__(self):
        return self.name
