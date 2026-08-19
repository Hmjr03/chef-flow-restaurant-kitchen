from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return self.username


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    dish_type = models.ForeignKey(
        DishType,
        on_delete=models.CASCADE,
        related_name="dishes",
    )
    cooks = models.ManyToManyField(
        Cook,
        related_name="dishes",
        blank=True,
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name="dishes",
        blank=True,
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
