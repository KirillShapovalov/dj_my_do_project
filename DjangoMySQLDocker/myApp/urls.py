from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('post/sync', views.post_sync, name='post-sync'),
    path('author/sync', views.author_sync, name='author-sync'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('author/create/', views.CreateAuthorView.as_view(), name='author-create'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-retrieve'),
    path('author/update/<int:pk>', views.AuthorDetailView.as_view(), name='author-update'),
    path('author/delete/<int:pk>', views.AuthorDetailView.as_view(), name='author-delete'),
    path('auth/', include('djoser.urls')),
    path('auth/token', obtain_auth_token, name='token'),
]
