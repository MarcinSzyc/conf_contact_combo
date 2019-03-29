from django.shortcuts import render, redirect
from django.views import View
from .models import Person, Address, Email, PhoneNumber
from .forms import PersonForm, AddressForm, EmailForm, PhoneNumberForm
from django.contrib import messages


class PersonAll(View):
    template = 'user_stories/person_all.html'
    all_people = Person.objects.select_related()

    def get(self, request):
        return render(request, self.template, {'person_list': self.all_people})


class NewPerson(View):
    template = 'user_stories/new_person.html'
    empty_Person = PersonForm()
    empty_Address = AddressForm()
    empty_Email = EmailForm()
    empty_Phone = PhoneNumberForm()

    def get(self, request):
        return render(request, self.template, {'person_form': self.empty_Person, 'address_form': self.empty_Address,
                                               'email_form': self.empty_Email, 'phone_form': self.empty_Phone})

    def post(self, request):
        filled_form = PersonForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            messages.success(request, 'Person created successfully!!!')
        else:
            messages.error(request, 'Upps, something went wrong!!!')
        return redirect('person_all')


class ModifyPersonView(View):
    template = 'user_stories/new_person.html'


    def post(self, request, id):
        person_instance = Person.objects.get(pk=id)
        filled_form = PersonForm(instance=person_instance)
        return render(request, self.template, {'form': filled_form})


class DeletePerson(View):

    def post(self, request, id):
        person_instance = Person.objects.get(pk=id)
        person_instance.delete()
        messages.error(request, 'Person deleted successfully!!!')
        return redirect('person_all')
