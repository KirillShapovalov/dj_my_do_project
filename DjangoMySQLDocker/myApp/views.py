from rest_framework import permissions
from dotenv import load_dotenv
from .models import Post, Author
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import serializers
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView
)
from .utils import sync_post, sync_author

load_dotenv()


@api_view(['GET'])
def post_sync(request):
    if request.method == 'GET':
        return Response(sync_post())


@api_view(['GET'])
def author_sync(request):
    if request.method == 'GET':
        return Response(sync_author())


class CreateAuthorView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class AuthorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]


class AuthorListView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer
    permission_classes = [permissions.AllowAny]


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.AllowAny]
