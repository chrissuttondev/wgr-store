from django.db import models


# Product Model
class Product(models.Model):
    CATERGORY_CHOICES = [
        ("men's clothing", "Men's Clothing"),
        ("women's clothing", "Women's Clothing"),
        ("jewelery", "Jewelery"),
        ("electronics", "Electronics"),
    ]

    title = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATERGORY_CHOICES)
    image_url = models.URLField(max_length=400)
    image_local = models.ImageField(null=True, blank=True)
    rate = models.FloatField(null=True, blank=True)
    count = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
