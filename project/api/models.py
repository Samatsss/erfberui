from django.db import models


class Meal(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.IntegerField()
    ingredients = models.ManyToManyField('Ingredients')

    def __str__(self):
        return self.title


class Ingredients(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
