from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_date(date):
    if date < timezone.now().date():
        raise ValidationError("Date cannot be in the past")


class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)
    capacity = models.IntegerField(blank=False)
    projector = models.BooleanField(blank=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    date = models.DateField(blank=False, unique=True, validators=[validate_date])
    comment = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING, blank=False)

    def __str__(self):
        return f"{self.room} {self.date}"
