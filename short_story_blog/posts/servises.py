from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.shortcuts import redirect


class ActivatedMixin:
    def has_permissions(self):
        return self.request.user.profile.confirmed == True

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            return redirect('users:vert')
        return super(ActivatedMixin, self).dispatch(
            request, *args, **kwargs)
