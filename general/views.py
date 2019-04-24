from django.shortcuts import render, redirect
from django.views import View
from .forms import UserLogin
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import resolve


def your_view(request):
    # resolve the url from the path
    url_name = resolve(request.path).url_name

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
            username = filled_form.cleaned_data.get('username')
            password = filled_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                messages.success(request, f'Witaj {user} !!')
                login(request, user)
                return redirect(self.request.META.get('HTTP_REFERER'))
            else:
                messages.error(request, 'Nie ma takiego użytkownika!')
                return redirect(self.request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Upps coś poszło nie tak!')
            return redirect(self.request.META.get('HTTP_REFERER'))


# Logout handling
class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('Home')
