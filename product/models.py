from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=300)
    surname = models.CharField(max_length=300)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.description

class Product(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    discount = models.FloatField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name
    