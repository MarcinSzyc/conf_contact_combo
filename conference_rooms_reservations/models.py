from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_date(date):
    if date < timezone.now().date():
        raise ValidationError("Date cannot be in the past")


class Room(models.Model):
    name = models.CharField('room name', max_length=100, unique=True)
    capacity = models.IntegerField('room capacity', blank=False, default=0)
    projector = models.BooleanField('projector', blank=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    date = models.DateField('reservation date', blank=False, validators=[validate_date])
    comment = models.TextField('comment', blank=True)
    room = models.ForeignKey('Room', on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return f"{self.room} {self.date}"
