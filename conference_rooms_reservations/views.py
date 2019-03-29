from django.shortcuts import render, redirect, HttpResponse
from .forms import NewRoomForm, NewReservationForm
from django.contrib import messages
from django.views.generic import View
from .models import Room, Reservation
from datetime import datetime


class Layout(View):
    def get(self, request):
        return redirect('conference_rooms_reservations:all_rooms')


class AddRoom(View):
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

class DeleteRoom(View):

    def get(self, request, **kwargs):
        instance = Room.objects.get(pk=self.kwargs['id'])
        instance.delete()
        messages.error(request, 'Room deleted successfully')
        return redirect('conference_rooms_reservations:all_rooms')


class ModifyRoom(View):
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


class ReservationView(View):
    form_class = NewReservationForm
    template = 'conference_rooms_reservations/reservations.html'

    def get(self, request, id):
        initial = Room.objects.values('name').get(pk=id)
        new_reservation_form = self.form_class(initial=initial)
        return render(request, self.template, locals())


class AddReservation(View):
    form_class = NewReservationForm

    def post(self, request):
        full_form = self.form_class(request.POST)
        if full_form.is_valid():
            full_form.save()
            messages.success(request, 'Room reserved successfully')
            return redirect('conference_rooms_reservations:all_rooms')
        else:
            messages.error(request,
                           'Room already bookeed. Check if the date is not in the past!')
            return redirect('conference_rooms_reservations:reserve_room_view', id=full_form.cleaned_data['room'].id)


class RoomSearch(View):
    form_class_reservations = NewReservationForm
    form_class_room = NewRoomForm
    template = 'conference_rooms_reservations/room_search.html'

    def get(self, request):
        empty_reservations = self.form_class_reservations
        empty_room = self.form_class_room
        return render(request, self.template,
                      {'form_reservations': empty_reservations,
                       'form_room': empty_room})

    def post(self, request):
        empty_reservations = self.form_class_reservations
        empty_room = self.form_class_room
        room_name = request.POST.get('name').capitalize()
        room_capacity = request.POST.get('capacity', default=0)
        room_date = request.POST.get('date', default=datetime.now().date())
        room_projector = request.POST.get('projector')

        global output, reserve
        output = Reservation.objects.select_related()
        reserve = False

        room_list = [item.name for item in Room.objects.select_related()]
        if room_name not in room_list:
            return render(request, self.template, {
                'output': f'Sala {room_name} NIE ISTNIEJE, spróbuj jeszcze raz!',
                'form_reservations': empty_reservations,
                'form_room': empty_room,
                'reserve': reserve,
            })
        else:
            if room_name is not None:
                output = output.filter(room__name=room_name)
            if room_capacity is not None:
                output = output.filter(room__capacity__gte=room_capacity)
            if room_projector is not None:
                if request.POST['projector'] == 'on':
                    output = output.filter(room__projector=True)
                else:
                    output = output.filter(room__projector=False)
            if room_date is not None:
                output = output.filter(date=room_date)
            if len(output) == 0:
                return render(request, self.template, {
                    'output': f'BRAK wolnych sal dla podanych kryteriów wyszukiwania',
                    'form_reservations': empty_reservations,
                    'form_room': empty_room,
                    'reserve': reserve,
                })
            else:
                reserve = True
                return render(request, self.template, {
                    'output': f'Sala {room_name} jest wolna w podanym terminie',
                    'form_reservations': empty_reservations,
                    'form_room': empty_room,
                    'reserve': reserve,
                })
