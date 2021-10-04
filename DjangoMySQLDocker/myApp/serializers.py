from rest_framework import serializers
from .models import Post, Author, Address, Geo, Company


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo
        fields = ['lat', 'lng']


class AddressSerializer(serializers.ModelSerializer):
    geo = GeoSerializer(many=True)

    class Meta:
        model = Address
        fields = ['street', 'suite', 'city', 'zipcode', 'geo']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'catchPhrase', 'bs']


class AuthorSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=True)
    company = CompanySerializer(many=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'username', 'email', 'address', 'phone', 'website', 'company']
        depth = 1


class AuthorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'username', 'email']
