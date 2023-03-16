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
    tax_price   = models.FloatField(null=True)
    discount_price = models.FloatField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name
    
    # get total price
    @property
    def total_price(self):
        return self.price + (self.tax_price or 0) - (self.discount_price or 0)


def upload_image_to_products(instance, filename):
    return f"product/{instance.product.name}/{filename}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_image_to_products)


    def __str__(self):
        return self.product.name