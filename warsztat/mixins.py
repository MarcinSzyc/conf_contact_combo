from django.contrib.auth.mixins import LoginRequiredMixin, PermissionDenied, redirect_to_login
from django.views import View
from django.contrib import messages


class MessageReturnMixin(LoginRequiredMixin, View):
    raise_exception = False
    permission_denied_message = 'You must be logged to perform this action!!'

    def get_permission_denied_message(self):
        """
        Override this method to override the permission_denied_message attribute.
        """
        return self.permission_denied_message

    def handle_no_permission(self):
        if self.raise_exception or self.request.user.is_authenticated:
            raise PermissionDenied(self.get_permission_denied_message())
        messages.error(self.request, self.permission_denied_message)
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
