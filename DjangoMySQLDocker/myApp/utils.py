import requests, os
from .models import Post, Author, Address, Geo, Company
from dotenv import load_dotenv
from rest_framework.response import Response

load_dotenv()


def sync_post():
    data = requests.get(os.getenv('url_posts'))
    data_j = data.json()
    post_list = []
    if data.status_code == 200:
        for i in data_j:
            post = Post(
                api_id=i['id'],
                title=i['title'],
                body=i['body']
            )
            try:
                post.author = Author.objects.get(pk=i['userId'])
            except:
                post.author = None
            post_list.append(post)
        Post.objects.bulk_create(post_list, ignore_conflicts=True)
        Post.objects.bulk_update(post_list, ['author', 'title', 'body', 'creation_date'])
    else:
        return Response('No response from API, please try again later.')

    quantity_of_rows = int(Post.objects.all().count())
    last_update_time = Post.objects.filter(api_id=quantity_of_rows).values('creation_date')

    context = {
        'quantity of rows': quantity_of_rows,
        'last update time': str(last_update_time[0]['creation_date'])
    }
    return context


def sync_author():
    data = requests.get(os.getenv('url_authors'))
    data_j = data.json()
    author_list = []
    address_list = []
    geo_list = []
    company_list = []
    if data.status_code == 200:
        for i in data_j:
            author = Author(
                api_id=i['id'],
                name=i['name'],
                username=i['username'],
                email=i['email'],
                phone=i['phone'],
                website=i['website']
            )
            author_list.append(author)
            address = Address(
                id=i['id'],
                street=i['address']['street'],
                suite=i['address']['suite'],
                city=i['address']['city'],
                zipcode=i['address']['zipcode'],
                author_id=i['id']
            )
            address_list.append(address)
            geo = Geo(
                id=i['id'],
                lat=i['address']['geo']['lat'],
                lng=i['address']['geo']['lng'],
                address_id=i['id']
            )
            geo_list.append(geo)
            company = Company(
                id=i['id'],
                name=i['company']['name'],
                catchPhrase=i['company']['catchPhrase'],
                bs=i['company']['bs'],
                author_id=i['id']
            )
            company_list.append(company)
        Author.objects.bulk_create(author_list, ignore_conflicts=True)
        Author.objects.bulk_update(author_list,
                                   ['name', 'username', 'email', 'phone', 'website', 'creation_date'])
        Address.objects.bulk_create(address_list, ignore_conflicts=True)
        Address.objects.bulk_update(address_list, ['street', 'suite', 'city', 'zipcode'])
        Geo.objects.bulk_create(geo_list, ignore_conflicts=True)
        Geo.objects.bulk_update(geo_list, ['lat', 'lng'])
        Company.objects.bulk_create(company_list, ignore_conflicts=True)
        Company.objects.bulk_update(company_list, ['name', 'catchPhrase', 'bs'])
    else:
        return Response('No response from API, please try again later.')

    last_author = Author.objects.values('api_id').last()['api_id']
    last_update_time = Author.objects.filter(api_id=last_author).values('creation_date')

    context = {
        'quantity of authors': last_author,
        'last update time': str(last_update_time[0]['creation_date'])
    }
    return context
