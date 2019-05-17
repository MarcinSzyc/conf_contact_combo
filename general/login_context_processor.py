from .forms import UserLogin, UserRegistration
from django.contrib.auth.forms import PasswordResetForm


def login_form_context(request):
    result = {
        'login_form': UserLogin,
        'register_form': UserRegistration,
        'password_reset_form': PasswordResetForm
    }
    return result
