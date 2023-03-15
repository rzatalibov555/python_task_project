
from django.contrib import admin

# Register your models here.


# Register your models here.

from product.models import Author, Product, ProductImage, Tag, Profile

# Register your models here.

admin.site.register([Tag,Author,Profile,Product,ProductImage])

