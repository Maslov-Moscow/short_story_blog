from django.shortcuts import redirect


class ActivatedMixin:
    """Проверка что аккаунт активирован"""
    def has_permissions(self):
        return self.request.user.profile.confirmed == True

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            return redirect('users:vert')
        return super(ActivatedMixin, self).dispatch(
            request, *args, **kwargs)
