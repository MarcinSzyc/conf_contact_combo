from django.shortcuts import render, redirect, HttpResponse
from .forms import NewRoomForm, NewReservationForm
from django.contrib import messages
from django.views.generic import DetailView
from .models import Room, Reservation


def layout(request):
    return redirect('/address')


class AddRoom(DetailView):
    form_class = NewRoomForm
    template = 'conference_rooms_reservations/add_room_view.html'

    def post(self, request):
        full_form = self.form_class(request.POST)
        if full_form.is_valid():
            full_form.save()
            messages.success(request, 'Room created successfully')
        else:
            messages.error(request, 'Room already exist!')
        return redirect('/address')

    def get(self, request):
        new_room_form = self.form_class
        return render(request, self.template, {'new_room_form': new_room_form})


class AllRooms(DetailView):
    template = 'conference_rooms_reservations/all_rooms_view.html'

    def get(self, request):
        rooms = Room.objects.all()
        return render(request, self.template, {'rooms': rooms})


class DeleteRoom(DetailView):

    def get(self, request, **kwargs):
        instance = Room.objects.get(pk=self.kwargs['id'])
        instance.delete()
        messages.error(request, 'Room deleted successfully')
        return redirect('/address')


class ModifyRoom(DetailView):
    template = 'conference_rooms_reservations/modify_room.html'
    form = NewRoomForm

    def get(self, request, id):
        instance = Room.objects.get(pk=id)
        filled_form = self.form(instance=instance)
        return render(request, self.template, {'form': filled_form, 'id': id})

    def post(self, request, id):
        instance = Room.objects.get(pk=id)
        full_form = self.form(request.POST, instance=instance)
        if full_form.is_valid():
            full_form.save()
            messages.success(request, 'Room modified successfully')
        return redirect('/address')


class ReservationView(DetailView):
    form_class = NewReservationForm
    template = 'conference_rooms_reservations/reservations.html'

    def post(self, request, id):
        initial = Room.objects.values('name').get(pk=id)
        new_reservation_form = self.form_class(initial=initial)
        return render(request, self.template, {'new_reservation_form': new_reservation_form, 'room': initial})


class AddReservation(DetailView):
    form_class = NewReservationForm

    def post(self, request):
        full_form = self.form_class(request.POST)
        if full_form.is_valid():
            full_form.save()
            messages.success(request, 'Room created successfully')
            return redirect('/address')
        else:
            messages.error(request,
                           'Sala jest już zarezerwowana na tą date lub sprawdź czy nie wybrałeś daty z przeszłości.')
            return redirect('/reservation')


class RoomSearch(DetailView):
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
        room_capacity = request.POST.get('capacity')
        room_date = request.POST.get('date')
        room_projector = request.POST.get('projector')

        global output, filter_by, reserve
        output = Reservation.objects.select_related()
        reserve = False
        filter_by = []

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
                output.filter(room__name=room_name)
            if room_capacity is not None:
                output.filter(room__capacity__gte=room_capacity)
            if room_projector is not None:
                if request.POST['projector'] == 'on':
                    output = output.filter(room__projector=True)
                else:
                    output = output.filter(room__projector=False)
            if room_date is not None:
                output.filter(date=room_date)
            if len(output) == 0:
                return render(request, self.template, {
                    'output': f'BRAK wolnych sal dla podanych kryteriów wyszukiwania',
                    'filter_by': filter_by,
                    'form_reservations': empty_reservations,
                    'form_room': empty_room,
                    'reserve': reserve,
                })
            else:
                reserve = True
                return render(request, self.template, {
                    'output': f'Sala {room_name} jest wolna w podanym terminie',
                    'filter_by': filter_by,
                    'form_reservations': empty_reservations,
                    'form_room': empty_room,
                    'reserve': reserve,
                })
