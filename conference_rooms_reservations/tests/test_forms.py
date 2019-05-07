from django.test import TestCase
from conference_rooms_reservations.forms import NewRoomForm, NewReservationForm


class NewRoomFormTests(TestCase):

    def test_room_name_field_label(self):
        form = NewRoomForm()
        form_field = form.fields['name'].label
        self.assertEquals(form_field, 'Room name')

    def test_room_capacity_field_label(self):
        form = NewRoomForm()
        form_field = form.fields['capacity'].label
        self.assertEquals(form_field, 'Room capacity')

    def test_room_projector_field_label(self):
        form = NewRoomForm()
        form_field = form.fields['projector'].label
        self.assertEquals(form_field, 'Projector')

    def test_for_name_field_widget(self):
        form = NewRoomForm()
        form_field = form.fields['name'].widget
        self.assertEquals(form_field.__class__.__name__, 'TextInput')

    def test_for_capacity_field_widget(self):
        form = NewRoomForm()
        form_field = form.fields['capacity'].widget
        self.assertEquals(form_field.__class__.__name__, 'NumberInput')

    def test_for_projector_field_widget(self):
        form = NewRoomForm()
        form_field = form.fields['projector'].widget
        self.assertEquals(form_field.__class__.__name__, 'CheckboxInput')

    def test_for_correct_bootstrap_widgets(self):
        form = NewRoomForm()
        name_field = form.fields['name'].widget
        capacity_field = form.fields['capacity'].widget
        projector_field = form.fields['projector'].widget
        self.assertEquals(name_field.attrs['class'], 'form-control mb-2 mr-sm-2')
        self.assertEquals(capacity_field.attrs['class'], 'form-control mb-2 mr-sm-2')
        self.assertEquals(projector_field.attrs['class'], 'form-control mb-2 mr-sm-2')


class NewReservationFormTests(TestCase):
    def test_reservation_name_field_label(self):
        form = NewReservationForm()
        form_field = form.fields['date'].label
        self.assertEquals(form_field, 'Reservation date')

    def test_reservation_capacity_field_label(self):
        form = NewReservationForm()
        form_field = form.fields['comment'].label
        self.assertEquals(form_field, 'Comment')

    def test_reservation_projector_field_label(self):
        form = NewReservationForm()
        form_field = form.fields['room'].label
        self.assertEquals(form_field, 'Room')

    def test_for_date_field_widget(self):
        form = NewReservationForm()
        form_field = form.fields['date'].widget
        self.assertEquals(form_field.__class__.__name__, 'SelectDateWidget')

    def test_for_correct_bootstrap_widgets(self):
        form = NewReservationForm()
        name_field = form.fields['date'].widget
        self.assertEquals(name_field.attrs['class'], 'form-control mb-2 mr-sm-2')
