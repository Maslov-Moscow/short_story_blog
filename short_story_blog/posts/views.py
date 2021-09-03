from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


def index(requst):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {"posts": posts}
    return render(requst, 'index.html', context)

def post(request, pk):
    return HttpResponse('succes')