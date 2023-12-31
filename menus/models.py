# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models


# Food and Drinks type so all food and drinks can be categorised
FOOD_CHOICE = (
    (0, "Starters"),
    (1, "Mains"),
    (2, "Steaks"),
    (3, "Desserts"),
    (4, "New")
)
DRINK_CHOICE = (
    (0, "White Wine"),
    (1, "Red Wine"),
    (2, "Rose Wine"),
    (3, "Prosecco"),
    (4, "Beers"),
    (5, "Cocktails"),
    (6, "Spirits"),
    (7, "New"),
)


# Model for Food items


class FoodSelection(models.Model):
    """
    A classs for all FoodSelection items in menu_food
    """

    food_id = models.AutoField(primary_key=True)
    name_food = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, unique=False)
    price = models.FloatField()
    food_choice = models.IntegerField(choices=FOOD_CHOICE, default=4)
    available = models.BooleanField(default=False)

    class Meta:
        ordering = ["-food_choice"]

    def __str__(self):
        return self.name_food


# Model for Drink items


class DrinkSelection(models.Model):
    """
    A classs for all DrinkSelection items in menu_drinks
    """

    drink_id = models.AutoField(primary_key=True)
    name_drink = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, unique=True)
    price = models.FloatField()
    drink_choice = models.IntegerField(choices=DRINK_CHOICE, default=7)
    available = models.BooleanField(default=False)

    class Meta:
        ordering = ["-available"]

    def __str__(self):
        return self.name_drink
