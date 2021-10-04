import requests
from rest_framework import permissions
from decouple import config
from .models import Post, Author, Address, Geo, Company
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import serializers
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView
)


@api_view(['GET'])
def post_sync(request):
    if request.method == 'GET':
        data = requests.get(config('url_posts'))
        data_j = data.json()
        post_list = []
        if data.status_code == 200:
            for i in data_j:
                post = Post(
                    user_id=i['userId'],
                    id=i['id'],
                    title=i['title'],
                    body=i['body']
                )
                post_list.append(post)
        Post.objects.bulk_create(post_list)
        quantity_of_rows = int(Post.objects.all().count())
        last_update_time = Post.objects.filter(id=quantity_of_rows).values('creation_date')

        context = {
            'quantity of rows': quantity_of_rows,
            'last update time': str(last_update_time[0]['creation_date'])
        }
        return Response(context)


@api_view(['GET'])
def author_sync(request):
    if request.method == 'GET':
        data = requests.get(config('url_authors'))
        data_j = data.json()
        author_list = []
        address_list = []
        geo_list = []
        company_list = []
        if data.status_code == 200:
            for i in data_j:
                author = Author(
                    id=i['id'],
                    name=i['name'],
                    username=i['username'],
                    email=i['email'],
                    phone=i['phone'],
                    website=i['website']
                )
                author_list.append(author)
                address = Address(
                    street=i['address']['street'],
                    suite=i['address']['suite'],
                    city=i['address']['city'],
                    zipcode=i['address']['zipcode'],
                    author_id=i['id']
                )
                address_list.append(address)
                geo = Geo(
                    lat=i['address']['geo']['lat'],
                    lng=i['address']['geo']['lng'],
                    address_id=i['id']
                )
                geo_list.append(geo)
                company = Company(
                    name=i['company']['name'],
                    catchPhrase=i['company']['catchPhrase'],
                    bs=i['company']['bs'],
                    author_id=i['id']
                )
                company_list.append(company)
        Author.objects.bulk_create(author_list)
        Address.objects.bulk_create(address_list)
        Geo.objects.bulk_create(geo_list)
        Company.objects.bulk_create(company_list)
        last_author = Author.objects.values('id').last()['id']
        last_update_time = Author.objects.filter(id=last_author).values('creation_date')

        context = {
            'quantity of authors': last_author,
            'last update time': str(last_update_time[0]['creation_date'])
        }
        return Response(context)


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