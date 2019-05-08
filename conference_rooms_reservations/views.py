from django.shortcuts import render, redirect
from .forms import NewRoomForm, NewReservationForm
from django.contrib import messages
from django.views.generic import View
from .models import Room, Reservation
from datetime import datetime
from warsztat.mixins import MessageReturnMixin



# Conference reservation main page view
class Layout(View):
    def get(self, request):
        return redirect('conference_rooms_reservations:all_rooms')


# Class view to show Add Room form and to accept data
class AddRoom(MessageReturnMixin, View):
    login_url = '/conf_rooms_reservations/address/'
    form_class = NewRoomForm
    template = 'conference_rooms_reservations/add_room_view.html'

    def post(self, request):
        full_form = self.form_class(request.POST)
        if full_form.is_valid():
            full_form.save()
            messages.success(request, 'Room created successfully')
        else:
            messages.error(request, 'Room already exist!')
        return redirect('conference_rooms_reservations:all_rooms')

    def get(self, request):
        new_room_form = self.form_class
        return render(request, self.template, locals())


# Class view to show All Rooms
class AllRooms(View):
    template = 'conference_rooms_reservations/all_rooms_view.html'

    def get(self, request):
        rooms = Room.objects.select_related()
        date_now = datetime.now().date()
        reserved_today = []
        for item in rooms:
            for reservation in item.reservation_set.all():
                if reservation.date == date_now:
                    reserved_today.append(item.name)
        return render(request, self.template, locals())


# Class view to process Delete Room request
class DeleteRoom(MessageReturnMixin, View):
    login_url = '/conf_rooms_reservations/address/'

    def get(self, request, **kwargs):
        instance = Room.objects.get(pk=self.kwargs['id'])
        instance.delete()
        messages.error(request, 'Room deleted successfully')
        return redirect('conference_rooms_reservations:all_rooms')


# Class view to show and process Modify Room request
class ModifyRoom(MessageReturnMixin, View):
    login_url = '/conf_rooms_reservations/address/'
    template = 'conference_rooms_reservations/modify_room.html'
    form = NewRoomForm

    def get(self, request, id):
        instance = Room.objects.get(pk=id)
        filled_form = self.form(instance=instance)
        return render(request, self.template, locals())

    def post(self, request, id):
        instance = Room.objects.get(pk=id)
        full_form = self.form(request.POST, instance=instance)
        if full_form.is_valid():
            full_form.save()
            messages.success(request, 'Room modified successfully')
        return redirect('conference_rooms_reservations:all_rooms')


# Class view to show detailed info about Room
class InfoView(View):
    template = 'conference_rooms_reservations/info_view.html'
    form = NewRoomForm

    def get(self, request, id):
        instance = Room.objects.get(pk=id)
        reservation = Reservation.objects.all().filter(room_id=id)
        return render(request, self.template, locals())


# Class view to show Room Reservation form
class ReservationView(View):
    form_class = NewReservationForm
    template = 'conference_rooms_reservations/reservations.html'

    def get(self, request, id):
        initial = Room.objects.get(pk=id)
        new_reservation_form = self.form_class(initial={'room': initial, 'date': datetime.today().date()})
        return render(request, self.template, locals())


# Class view to process new Room Reservation
class AddReservation(View):
    form_class = NewReservationForm

    def post(self, request):
        full_form = self.form_class(request.POST)
        if full_form.is_valid():
            room_id = full_form.cleaned_data['room'].id
            all_reservations = [item.date for item in Reservation.objects.all().filter(room_id=room_id)]
            if full_form.cleaned_data["date"] in all_reservations:
                messages.error(request, 'Room already booked. Try different date or change room!')
                return redirect('conference_rooms_reservations:reserve_room_view', id=room_id)
            else:
                full_form.save()
                messages.success(request, 'Room reserved successfully')
                return redirect('conference_rooms_reservations:all_rooms')
        else:
            messages.error(request, f'Invalid data or date is in the past!')
            return redirect('conference_rooms_reservations:reserve_room_view', id=request.POST['room'])


# Class view to show and process Room Search
class RoomSearch(View):
    form_class_reservations = NewReservationForm
    form_class_room = NewRoomForm
    template = 'conference_rooms_reservations/room_search.html'
    global output

    def get(self, request):
        empty_reservations = self.form_class_reservations(initial={'date': datetime.today().date()})
        empty_room = self.form_class_room
        return render(request, self.template, locals())

    def post(self, request):
        control = True
        empty_reservations = self.form_class_reservations(initial={'date': datetime.today().date()})
        empty_room = self.form_class_room
        room_name = request.POST.get('name')
        room_capacity = request.POST.get('capacity', default=0)
        date_day = int(request.POST.get('date_day'))
        date_month = int(request.POST.get('date_month'))
        date_year = int(request.POST.get('date_year'))
        room_date = datetime(year=date_year, day=date_day, month=date_month).date()
        room_projector = request.POST.get('projector')

        output = Room.objects.select_related()

        if room_name.upper() in [item.name.upper() for item in output]:
            output = output.filter(name=room_name.capitalize())
        elif room_name == '':
            output = output
        else:
            messages.error(request, "Room with this name does not exist!!")

        if room_capacity is not None:
            output = output.filter(capacity__gte=room_capacity)

        if room_projector == 'on':
            output = output.filter(projector=True)
        else:
            output = output.filter(projector=False)

        for item in output:
            for reservation in item.reservation_set.all():
                if reservation.date == room_date:
                    output = output.exclude(name=item.name)

        return render(request, self.template, locals())
