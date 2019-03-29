from django.forms import ModelForm, DateInput
from django import forms
from conference_rooms_reservations.models import Room, Reservation


class NewRoomForm(ModelForm):
    class Meta:
        model = Room
        exclude = []


class NewReservationForm(ModelForm):
    class Meta:
        model = Reservation
        exclude = []
        widgets = {
            'date': DateInput(attrs={'type': 'date'})
        }
