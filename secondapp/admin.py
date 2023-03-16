from django.contrib import admin

# Register your models here.
from .models import Author, AuthorProfile

# admin.site.register([Author,AuthorProfile])
admin.site.register(Author)
admin.site.register(AuthorProfile)
# admin.site.register(SocialMedia)