from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name="index"),
    path('profile/<str:username>/', views.profile, name='profile'),
    # path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new', views.PostCreateView.as_view(), name='new'),
    path('post/edit/<int:pk>', views.EditPostView.as_view(), name='edit')
]
