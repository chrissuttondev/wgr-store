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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.URLField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
