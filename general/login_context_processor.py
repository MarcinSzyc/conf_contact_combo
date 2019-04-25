from .forms import UserLogin, UserRegistration


def login_form_context(request):
    result = {
        'login_form': UserLogin,
        'register_form': UserRegistration
    }
    return result
