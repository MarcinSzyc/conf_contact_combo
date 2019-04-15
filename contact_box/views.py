from django.shortcuts import render, redirect
from django.views import View
from .models import Person, Address, Email, PhoneNumber
from .forms import PersonForm, AddressForm, EmailForm, PhoneNumberForm
from django.contrib import messages


class PersonAll(View):
    template = 'contact_box/person_all.html'

    def get(self, request):
        all_people = Person.objects.select_related()
        return render(request, self.template, locals())


class NewPerson(View):
    template = 'contact_box/new_person.html'

    def get(self, request):
        empty_person = PersonForm
        return render(request, self.template, locals())

    def post(self, request):
        filled_form = PersonForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            messages.success(request, 'Person created successfully!!!')
        else:
            messages.error(request, 'Upps, something went wrong!!!')
        return redirect('contact_box:person_all')


class ModifyPersonView(View):
    template = 'contact_box/modify_person.html'

    def get(self, request, id):
        person_instance = Person.objects.get(pk=id)
        add_phone = PhoneNumberForm
        add_email = EmailForm
        pre_filled_person_form = PersonForm(instance=person_instance)
        return render(request, self.template, locals())

    def post(self, request):
        filled_form = PersonForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            messages.success(request, 'Person updated successfully!!!')
        else:
            messages.error(request, 'Upps, something went wrong!!!')


class DeletePerson(View):

    def get(self, request, id):
        person_instance = Person.objects.get(pk=id)
        person_instance.delete()
        messages.error(request, 'Person deleted successfully!!!')
        return redirect('contact_box:person_all')


class NewEmail(View):
    template = 'contact_box/new_email_view.html'

    def get(self, request):
        empty_email = EmailForm
        return render(request, self.template, locals())

    def post(self, request):
        filled_form = EmailForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            messages.success(request, 'Email created successfully!!!')
        else:
            messages.error(request, 'Upps, something went wrong!!!')
        return redirect('contact_box:new_email')


class NewAddress(View):
    template = 'contact_box/new_address_view.html'

    def get(self, request):
        empty_address = AddressForm
        return render(request, self.template, locals())

    def post(self, request):
        filled_form = AddressForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            messages.success(request, 'Address created successfully!!!')
        else:
            messages.error(request, 'Upps, something went wrong!!!')
        return redirect('contact_box:new_address')


class NewPhoneNumber(View):
    template = 'contact_box/new_phone_number_view.html'

    def get(self, request):
        empty_phone_number = PhoneNumberForm
        return render(request, self.template, locals())

    def post(self, request):
        filled_form = PhoneNumberForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            messages.success(request, 'Phone number created successfully!!!')
        else:
            messages.error(request, 'Upps, something went wrong!!!')
        return redirect('contact_box:new_phone_number')
