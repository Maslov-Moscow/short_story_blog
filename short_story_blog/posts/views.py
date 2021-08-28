from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(requst):
    context = { "a": [1,2,3]}
    return render(requst, 'index.html', context)

def post(request, pk):
    return HttpResponse('succes')