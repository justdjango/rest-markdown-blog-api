from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/create/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<slug>/update/', views.PostUpdateView.as_view(), name='post-update')
]