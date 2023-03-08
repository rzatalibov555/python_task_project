from django.contrib import admin

# Register your models here.
from .models import Author, AuthorProfile, UserProfileTest

# admin.site.register([Author,AuthorProfile])
admin.site.register(Author)
admin.site.register(AuthorProfile)
admin.site.register(UserProfileTest)
# admin.site.register(SocialMedia) # burda add elemek olmur
