from django.db import models


class Author(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    username = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=50, default=None)
    phone = models.CharField(max_length=50, default=None)
    website = models.CharField(max_length=50, default=None)
    creation_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return self.username

    objects = models.Manager()


class Address(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    street = models.CharField(max_length=100)
    suite = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name='address', on_delete=models.CASCADE)

    def __str__(self):
        return self.city

    objects = models.Manager()


class Geo(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, null=False, blank=False)
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)
    address = models.ForeignKey(Address, related_name='geo', on_delete=models.CASCADE)

    def __str__(self):
        return self.lat

    objects = models.Manager()


class Company(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, null=False, blank=False)
    name = models.CharField(max_length=100)
    catchPhrase = models.CharField(max_length=100)
    bs = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name='company', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    objects = models.Manager()


class Post(models.Model):
    user = models.ForeignKey(Author, null=True, blank=True, on_delete=models.CASCADE)
    api_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    body = models.CharField(max_length=1000, null=False, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return self.title

    objects = models.Manager()
