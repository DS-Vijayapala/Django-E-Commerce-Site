from django.db import models

# Create your models here.

options = (
    ('fashion', 'Fashion'),
    ('electronics', 'Electronics'),
    ('sports', 'Sports'),
    ('Gaming', 'Gaming'),
)

class Product(models.Model):

    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    catogaory = models.CharField(max_length=200 , choices=options)
    description = models.TextField()
    image = models.CharField(max_length=3000)

    def __str__(self):
        return self.title
