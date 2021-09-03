from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name="index"),
    path('posts/<int:pk>', views.post, name="posts")
]