from django.forms import ModelForm, Select, CheckboxInput, TextInput, SelectMultiple, NumberInput, SelectDateWidget
from conference_rooms_reservations.models import Room, Reservation
from django import forms


class NewRoomForm(ModelForm):
    class Meta:
        model = Room
        widgets = {
            'name': TextInput(attrs={'class': 'form-control mb-2 mr-sm-2'}),
            'capacity': NumberInput(attrs={'class': 'form-control mb-2 mr-sm-2'}),
            'projector': CheckboxInput(attrs={'class': 'form-control mb-2 mr-sm-2'})
        }
        exclude = []


class NewReservationForm(ModelForm):
    class Meta:
        model = Reservation
        widgets = {
            'date': SelectDateWidget(attrs={'class': 'form-control mb-2 mr-sm-2'})
        }
        exclude = []

    # date = forms.DateField(
    #     widget=forms.SelectDateWidget(
    #         # empty_label=("Choose Year", "Choose Month", "Choose Day"),
    #         # attrs={'class', 'custom-select mr-sm-2'}
    #     ),
    # )
    # widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'text'}),
    # input_formats=('%d/%mmm/%Y',))
