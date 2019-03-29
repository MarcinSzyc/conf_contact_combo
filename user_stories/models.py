from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    address = models.ForeignKey('Address', on_delete=models.DO_NOTHING, blank=False)

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Address(models.Model):
    city = models.CharField(max_length=32)
    street = models.CharField(max_length=64)
    home_number = models.IntegerField()
    flat_number = models.IntegerField(blank=True)


class PhoneNumber(models.Model):
    mobile_types = (
        (0, "home"),
        (1, "mobile"),
        (2, "work"),
    )
    phone_number = models.IntegerField()
    type = models.IntegerField(choices=mobile_types, default=1)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.phone_number}'


class Email(models.Model):
    email_type = (
        (0, "private"),
        (1, "work"),
    )
    email_address = models.EmailField()
    type = models.IntegerField(choices=email_type)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.email_address

class Group(models.Model):
    name = models.CharField(max_length=100, blank=False)
    person = models.ManyToManyField(Person)
