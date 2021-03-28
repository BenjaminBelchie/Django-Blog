from django.contrib import admin
from django.urls import path
from . import views
from .views import PostListViewD, PostListViewA,PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, UserListAll, home

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('test/', views.test, name='blog-test'),
    path('blog', PostListViewD.as_view(), name='MessageBoard-home'),
    path('post/a', PostListViewA.as_view(), name='MessageBoard-home-acending'),
    path('user/all', UserListAll.as_view(), name='users-list'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('search/', views.get_queryset, name='MessageBoard-search'),
]