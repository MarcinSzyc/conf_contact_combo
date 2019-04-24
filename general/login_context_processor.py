from django.shortcuts import render, redirect
from .forms import UserLogin


def login_form_context(request):
    result = {'login_form': UserLogin}
    return result
