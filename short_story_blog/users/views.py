from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponse
from .forms import CreationForm, VerificationForm
from django.contrib.auth import get_user_model
from django.shortcuts import redirect

User = get_user_model()


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'


def PasswordCheck(request, ):
    if request.method == "POST":
        form = VerificationForm(request.POST)
        if form.is_valid():
            if request.user.profile.code == form.cleaned_data['password']:
                profile = request.user.profile
                profile.confirmed = True
                profile.save()
                return redirect('posts:new')
            else:
                error = 'Не верный код'
                return render(request, 'users/vertification.html', {'form': form, 'error': error})

    else:
        form = VerificationForm
        return render(request, 'users/vertification.html', {'form': form})
