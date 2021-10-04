from django.contrib import admin
from .models import Author, Address, Geo, Company, Post

admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Geo)
admin.site.register(Company)
admin.site.register(Post)
