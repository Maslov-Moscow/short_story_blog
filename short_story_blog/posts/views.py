from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied

from .forms import PostForm
from .models import Post, User
from .servises import ActivatedMixin


class IndexListView(ListView):
    """Стартовая страница"""
    model = Post
    paginate_by = 10
    template_name = "index.html"
    ordering = ['-pub_date']


def profile(request, username):
    """Страница профиля"""
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user)
    post_count = posts.count()
    context = {
        "user": user,
        "posts": posts,
        "counter": post_count
    }
    return render(request, 'posts/profile.html', context)


#


class PostDetailView(DetailView):
    """Страница отдельного поста"""
    model = Post
    template_name = "posts/post_detail.html"


class PostCreateView(LoginRequiredMixin, ActivatedMixin, CreateView):
    """Страница создания поста"""
    form_class = PostForm
    template_name = 'posts/new.html'
    success_url = '/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        return super(PostCreateView, self).form_valid(form)


class EditPostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Страница редактирования поста"""
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


def page_not_found(request, exception):
    return render(request, "misc/404.html", {"path": request.path}, status=404)


def server_error(request):
    return render(request, "misc/500.html", status=500)
