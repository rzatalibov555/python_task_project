from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=300)
    surname = models.CharField(max_length=300)

class SocialMedia(models.Model):
    facebook  = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin  = models.URLField(blank=True, null=True)


    class Meta:
        abstract = True

class AuthorProfile(Author, SocialMedia):
    address = models.TextField(blank=True, null=True)


class UserProfileTest(Author, SocialMedia):
    bio = models.TextField(blank=True, null=True)


