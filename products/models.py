from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Products(models.Model):
    title = models.CharField(max_length=300)
    price = models.FloatField()
    description = models.CharField(max_length=500)
    category = models.ForeignKey('category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    image_url = models.URLField()
    image = models.ImageField(null=True, blank=True)
    rating_rate = models.FloatField(null=True, blank=True)
    rating_count = models.IntegerField(null=True, blank=True,)

    def __str__(self):
        return self.title
