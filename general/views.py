from django.shortcuts import render, redirect
from django.views import View
from .forms import UserLogin, UserRegistration
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordResetView
from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse_lazy


# Main page view
class Home(View):
    template = 'general/main_page.html'

    def get(self, request):
        return render(request, self.template)


# Login handling
class Login(View):
    template = 'general/login_page.html'

    def get(self, request):
        empty_form = UserLogin
        return render(request, self.template, locals())

    def post(self, request):
        filled_form = UserLogin(request.POST)
        if filled_form.is_valid():
            username = filled_form.cleaned_data.get('username_field')
            password = filled_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                messages.success(request, f'Hello {user} !!')
                login(request, user)
                return redirect(self.request.META.get('HTTP_REFERER'))
            else:
                messages.error(request, 'There is no such username in the database!')
                return redirect(self.request.META.get('HTTP_REFERER'))
        else:
            error_list = [item for item in filled_form.errors.values()]
            messages.error(request, f'Upps something went wrong!! \n {error_list[0]}')
            return redirect(self.request.META.get('HTTP_REFERER'))


# Logout handling
class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('Home')


# Register handling
class Register(View):
    template = 'general/login_page.html'

    def get(self, request):
        empty_form = UserRegistration
        return render(request, self.template, locals())

    def post(self, request):
        filled_form = UserRegistration(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            messages.success(request, 'User created!')
            return redirect(self.request.META.get('HTTP_REFERER'))
        else:
            error_list = [item for item in filled_form.errors.values()]
            messages.error(request, f'Upps something went wrong!! \n {error_list}')
            return redirect(self.request.META.get('HTTP_REFERER'))


class ModifiedPasswordResetView(PasswordResetView):
    success_url = reverse_lazy('password_reset_done')

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        if not self.success_url:
            raise ImproperlyConfigured("No URL to redirect to. Provide a success_url.")
        else:
            messages.info(self.request,
                             '''We've emailed you instructions for setting your password, if an account exists with the email you entered. You should receive them shortly. \n
                             If you don't receive an email, please make sure you've entered the address you registered with,and check your spam folder.''')
        return str(self.request.META.get('HTTP_REFERER'))  # success_url may be lazy
