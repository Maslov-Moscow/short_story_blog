from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from .models import Post, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
# from django.shortcuts import

def index(requst):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {"posts": posts}
    return render(requst, 'index.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user)
    post_count = posts.count()
    context = {
        "user": user,
        "posts": posts,
        "counter": post_count
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {"post": post}
    return render(request, 'posts/post_detail.html', context)

class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"



class PostCreateView(LoginRequiredMixin,CreateView):
    form_class = PostForm
    template_name = 'posts/new.html'
    success_url = '/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        return super(PostCreateView, self).form_valid(form)


class EditPostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'posts/new.html'
    fields = ['text']

    def test_func(self):
        obj = self.get_object()
        if obj.author == self.request.user:
            return True
        raise PermissionDenied



    def get_success_url(self):
        pk = self.kwargs["pk"]
        return f'/posts/{pk}'
