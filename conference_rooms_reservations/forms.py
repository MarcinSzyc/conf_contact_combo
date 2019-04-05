from django.forms import ModelForm
from conference_rooms_reservations.models import Room, Reservation
from django import forms


class NewRoomForm(ModelForm):
    class Meta:
        model = Room
        exclude = []


class NewReservationForm(ModelForm):
    class Meta:
        model = Reservation
        exclude = []

    date = forms.DateField(
        widget=forms.SelectDateWidget(
            empty_label=("Choose Year", "Choose Month", "Choose Day"),
        ),
    )
    # widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'text'}),
    # input_formats=('%d/%mmm/%Y',))
