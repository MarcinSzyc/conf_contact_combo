from django.shortcuts import render, redirect
from django.views import View
from .models import Person, Address, Email, PhoneNumber, Group
from .forms import PersonForm, AddressForm, EmailForm, PhoneNumberForm, GroupForm
from django.contrib import messages
from warsztat.mixins import MessageReturnMixin


class PersonAll(View):
    template = 'contact_box/person_all.html'

    def get(self, request):
        all_people = Person.objects.select_related()
        return render(request, self.template, locals())


class NewPerson(MessageReturnMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login/'
    template = 'contact_box/new_person.html'

    def get(self, request):
        people = Person.objects.all()
        empty_person = PersonForm
        return render(request, self.template, locals())

    def post(self, request):
        filled_form = PersonForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            messages.success(request, 'Person created successfully!!!')
        else:
            error_list = [item for item in filled_form.errors.values()]
            messages.error(request, f'Upps, something went wrong!!! \n {error_list}')
        return redirect('contact_box:person_all')


class ModifyPersonView(MessageReturnMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login/'
    template = 'contact_box/modify_person.html'

    def get(self, request, id):
        person_instance = Person.objects.get(pk=id)
        add_phone = PhoneNumberForm
        add_email = EmailForm
        add_group = GroupForm
        pre_filled_person_form = PersonForm(instance=person_instance)
        return render(request, self.template, locals())

    def post(self, request, id):
        person_instance = Person.objects.get(pk=id)
        filled_form = PersonForm(data=request.POST, instance=person_instance)
        if filled_form.is_valid():
            filled_form.save()
            messages.success(request, 'Person updated successfully!!!')
        else:
            messages.error(request, 'Upps, something went wrong!!!')
        return redirect('contact_box:person_all')


class DeletePerson(MessageReturnMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login/'

    def get(self, request, id):
        person_instance = Person.objects.get(pk=id)
        person_instance.delete()
        messages.error(request, 'Person deleted successfully!!!')
        return redirect('contact_box:person_all')


class NewEmail(MessageReturnMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login/'
    template = 'contact_box/new_email_view.html'

    def get(self, request):
        emails = Email.objects.all()
        empty_email = EmailForm
        return render(request, self.template, locals())

    def post(self, request):
        filled_form = EmailForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            messages.success(request, 'Email created successfully!!!')
        else:
            messages.error(request, 'Upps, something went wrong!!!')
        return redirect('contact_box:person_all')


class NewAddress(MessageReturnMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login/'
    template = 'contact_box/new_address_view.html'

    def get(self, request):
        addresses = Address.objects.all()
        empty_address = AddressForm
        return render(request, self.template, locals())

    def post(self, request):
        filled_form = AddressForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            messages.success(request, 'Address created successfully!!!')
        else:
            messages.error(request, 'Upps, something went wrong!!!')
        return redirect('contact_box:person_all')


class NewPhoneNumber(MessageReturnMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login/'
    template = 'contact_box/new_phone_number_view.html'

    def get(self, request):
        numbers = PhoneNumber.objects.all()
        empty_phone_number = PhoneNumberForm
        return render(request, self.template, locals())

    def post(self, request):
        filled_form = PhoneNumberForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            messages.success(request, 'Phone number created successfully!!!')
        else:
            error_list = [item for item in filled_form.errors.values()]
            messages.error(request, f'Upps, something went wrong!!! \n {error_list}')
        return redirect('contact_box:person_all')


class NewGroup(MessageReturnMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login/'
    template = 'contact_box/new_group_view.html'

    def get(self, request):
        groups = Group.objects.all()
        empty_group = GroupForm
        return render(request, self.template, locals())

    def post(self, request):
        filled_form = GroupForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            messages.success(request, 'Group created successfully!!!')
        else:
            messages.error(request, 'Upps, something went wrong!!!')
        return redirect('contact_box:person_all')


class DeleteGroup(MessageReturnMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login/'

    def get(self, request, id):
        group_instance = Group.objects.get(pk=id)
        group_instance.delete()
        messages.error(request, 'Group deleted successfully!!!')
        return redirect('contact_box:person_all')


class DeleteEmail(MessageReturnMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login/'

    def get(self, request, id):
        email_instance = Email.objects.get(pk=id)
        email_instance.delete()
        messages.error(request, 'Email address deleted successfully!!!')
        return redirect('contact_box:person_all')


#
class DeletePhone(MessageReturnMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login/'

    def get(self, request, id):
        phone_instance = PhoneNumber.objects.get(pk=id)
        phone_instance.delete()
        messages.error(request, 'Phone number deleted successfully!!!')
        return redirect('contact_box:person_all')


class DeleteAddress(MessageReturnMixin, View):
    login_url = '/login/'
    redirect_field_name = 'login/'

    def get(self, request, id):
        address_instance = Address.objects.get(pk=id)
        address_instance.delete()
        messages.error(request, 'Address deleted successfully!!!')
        return redirect('contact_box:person_all')




