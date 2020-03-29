from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    toppings = models.ManyToManyField('Topping')

    def __str__(self):
        return self.name

class Topping(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
