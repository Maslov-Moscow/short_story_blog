from django.views.generic import CreateView ,FormView
from django.urls import reverse_lazy
from django.shortcuts import render , HttpResponse
from .forms import CreationForm ,VerificationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'



def PasswordCheck(request,):
    if request.method == "POST":
        form =  VerificationForm(request.POST)
        if form.is_valid():
            s = request.user.profile.code == form.cleaned_data['password']
            
            return HttpResponse(s)
        else:
            return HttpResponse("ssd")

    else:

        form = VerificationForm
        return render(request,'users/vertification.html',{'form':form})