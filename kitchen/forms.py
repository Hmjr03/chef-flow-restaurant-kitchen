from django import forms
from django.contrib.auth.forms import UserCreationForm

from kitchen.models import (
    Cook,
    Dish,
    DishType,
    Ingredient,
)


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = [
            "name",
            "description",
            "price",
            "dish_type",
            "cooks",
            "ingredients",
        ]

        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 4,
                    "class": "form-control",
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "step": "0.01",
                    "class": "form-control",
                }
            ),
        }


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = [
            "name",
        ]


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = [
            "name",
        ]


class CookCreationForm(UserCreationForm):
    class Meta:
        model = Cook
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
            "password1",
            "password2",
        ]


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        ]
