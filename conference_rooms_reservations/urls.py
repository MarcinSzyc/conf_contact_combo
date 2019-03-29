"""warsztat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from conference_rooms_reservations.views import (
    AddRoom, AllRooms, ModifyRoom, DeleteRoom,
    AddReservation, ReservationView, RoomSearch, Layout, InfoView)

app_name = "conference_rooms_reservations"

urlpatterns = [
    path('', Layout.as_view(), name='layout'),
    path('room/add', AddRoom.as_view(), name='add_room'),
    path('room/modify/<int:id>', ModifyRoom.as_view(), name='modify_room'),
    path('room/delete/<int:id>', DeleteRoom.as_view(), name='delete_room'),
    path('room/info/<int:id>', InfoView.as_view(), name='info_view'),
    path('address/', AllRooms.as_view(), name='all_rooms'),
    path('reservation/<int:id>', ReservationView.as_view(), name='reserve_room_view'),
    path('reservation/', AddReservation.as_view(), name='add_reservation'),
    path('search/', RoomSearch.as_view(), name='room_search'),
]
