from django.db import models

# Create your models here.

options = (
    ('fashion', 'Fashion'),
    ('electronics', 'Electronics'),
    ('sports', 'Sports'),
    ('Gaming', 'Gaming'),
)


class Product(models.Model):
    """ This model is used to store the product details"""

    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    catogaory = models.CharField(max_length=200, choices=options)
    description = models.TextField()
    image = models.CharField(max_length=3000)

    def __str__(self):
        return self.title


class Order(models.Model):
    """ This model is used to store the order details """

    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=2000)
    email = models.CharField(max_length=2000)
    address = models.CharField(max_length=3000)
    city = models.CharField(max_length=2000)
    state = models.CharField(max_length=2000)
    zip_code = models.CharField(max_length=200)
    total = models.CharField(max_length=2000)

    def __str__(self):
        return self.name
